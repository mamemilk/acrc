module cpu_top(
   input        clk
  ,input        rstn
  ,output [3:0] address
  ,input  [7:0] instruction
  ,input  [3:0] in
  ,output [3:0] out 
);

  wire    [3:0] opecode;
  wire    [3:0] operand;
  wire    [3:0] register;
  wire    [3:0] immidiate;

  wire    [3:0] alu;
  wire    [3:0] y;

  wire    [3:0] load, load_d;

  reg     [3:0] r_a, r_b, r_in, r_pc, r_out;
  
  wire          c; //carryout flag
  reg           r_c; 

  wire    [1:0] ds, ds_d;
  wire          select_b, select_a;
  assign select_b = ds[1];
  assign select_a = ds[0];

  assign opecode   = instruction[7:4];
  assign immidiate = instruction[3:0];

  assign address   = r_pc; 
  assign out       = r_out;

  // select_B, select_Aの順番で書かれているので要注意
  function [3:0] dataselector;
    input         a;
    input         b;
    input [3:0]   c0; //reg A
    input [3:0]   c1; //reg B
    input [3:0]   c2; //reg input
    input [3:0]   c3; //0x0 data 

    // wire sel;
    // assign sel = {select_b, select_a};
    case({b, a})
      2'b11:        dataselector = c3; //0x0, only immidiate 
      2'b01:        dataselector = c2; //reg input
      2'b10:        dataselector = c1; //reg B
      2'b00:        dataselector = c0; //reg A
      default:      dataselector = 'd0;
    endcase
    // always@(*) begin
    //   if      ( select_b &&  select_a)  dataselector = c3;
    //   else if ( select_b && ~select_a)  dataselector = c2;
    //   else if (~select_b &&  select_a)  dataselector = c1;
    //   else if (~select_b && ~select_a)  dataselector = c0;
    //   else                              dataselector = 'd0;
    // end
  endfunction

  assign y = dataselector(select_b, select_a,
                          r_a,
                          r_b,
                          r_in,
                          'd0);

  // ALUは足すだけ
  assign {c, alu} = y + immidiate;


  // LOAD, registers
  always @(negedge rstn or posedge clk) begin
    if     (~rstn)       r_a <= #1 4'd0;
    else if(load[0])     r_a <= #1 alu;
  end
  always @(negedge rstn or posedge clk) begin
    if     (~rstn)       r_b <= #1 4'd0;
    else if(load[1])     r_b <= #1 alu;
  end
  always @(negedge rstn or posedge clk) begin
    if     (~rstn)       r_out <= #1 4'd0;
    else if(load[2])     r_out <= #1 alu;
  end
  always @(negedge rstn or posedge clk) begin
    if     (~rstn)       r_pc <= #1 4'd0;
    else if(load[3])     r_pc <= #1 alu;
    else                 r_pc <= #1 r_pc + 'd1;
  end

  // Carry out
  always @(negedge rstn or posedge clk) begin
    if     (~rstn)       r_c <= #1 1'b0;
    else if(c)           r_c <= #1 1'b1;
    else                 r_c <= #1 1'b0;
  end

  
  always @(negedge rstn or posedge clk) begin
    if  (~rstn)       r_in <= #1 'd0;
    else              r_in <= #1 in;
  end


  // ,input  [4-1:0] opecode
  // ,input          cflag
  // ,output [2-1:0] ds
  // ,output [4-1:0] register 
  cpu_decoder cpu_decoder0( clk
                           ,rstn
                           ,opecode
                           ,~r_c
                           ,ds
                           ,load 
                           ,ds_d
                           ,load_d 
                          );


endmodule 

module test_cpu_top();

  reg clk;
  reg rstn;

  wire [3:0] address;
  wire [7:0] data, data_d;

  wire [3:0] dout;
  reg  [3:0] din;


  initial begin
    clk = 0;
    @(posedge rstn);
    #20;
    clk = 1;
    forever #5 clk = ~clk;
  end

  initial begin
    rstn = 0;
    din  = 0;
    #30 rstn = 1;

    @(posedge clk);
    din = 4'b1010;
  end



  initial begin
    #2600 $finish();
  end


  cpu_top cpu_top0( clk         // input          clk
                   ,rstn        // ,input          rstn
                   ,address     // ,output [4-1:0] address
                   ,data // ,input  [8-1:0] instruction
                   ,din          // ,output [4-1:0] in
                   ,dout         // ,output [4-1:0] out
                  );


  cpu_rom cpu_rom0( clk
                   ,rstn
                   ,address
                   ,data
                   ,data_d
                  );

  initial begin
    $dumpfile("cpu_top_test.vcd");
    $dumpvars(0, test_cpu_top);
  end


endmodule

