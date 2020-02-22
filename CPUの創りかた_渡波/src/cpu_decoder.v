module cpu_decoder(
   input        clk
  ,input        rstn
  ,input  [3:0] opecode
  ,input        cflag
  ,output [1:0] ds
  ,output [3:0] register 
  ,output [1:0] ds_d
  ,output [3:0] register_d
);

  reg  [1:0] r_ds;
  reg  [3:0] r_register;

  wire [1:0] ds;
  wire [3:0] register;

  wire [5:0] decoder_out;

  function [5:0] decoder; //ds[1] ds[0] load[3][2][1][0]
    input [3:0] code; 
    input       flag; 
    case(code)                    
      4'b0000:        decoder = 6'b000001 ; //ADD A,Im, data select A
      4'b0001:        decoder = 6'b010001 ; //MOV A,B   data select B
      4'b0010:        decoder = 6'b100001 ; //IN  A     data select IN
      4'b0011:        decoder = 6'b110001 ; //MOV A,Im  data select 0 
      4'b0100:        decoder = 6'b000010 ; //MOV B,A   data select A
      4'b0101:        decoder = 6'b010010 ; //ADD B,Im  data select B
      4'b0110:        decoder = 6'b100010 ; //IN  B     data select IN
      4'b0111:        decoder = 6'b110010 ; //MOV B,Im  data select 0
    //4'b1000:        decoder = 6'b ; 
      4'b1001:        decoder = 6'b010100 ; //OUT B     data select B
    //4'b1010:        decoder = 6'b ; 
      4'b1011:        decoder = 6'b110100 ; //OUT Im    data select 0
    //4'b1100:        decoder = 6'b ; 
    //4'b1101:        decoder = 6'b ; 
      4'b1110:        decoder = {2'b11, flag, 3'b000} ; //JNC(C=0)JNC(C=1) data select 0
      4'b1111:        decoder = 6'b111000 ; //JMP
      default:        decoder = 6'bxxxxxx ;
    endcase
  endfunction

  assign decoder_out = decoder(opecode, cflag);

  always @(negedge rstn or posedge clk)  begin
    if (~rstn) begin
      r_ds       <= #1 2'b0;//decoder_out[5:4];
      r_register <= #1 4'b0;//decoder_out[3:0];
    end else begin
      r_ds       <= #1 ds;
      r_register <= #1 register;
    end
  end

  assign ds         = decoder_out[5:4];
  assign register   = decoder_out[3:0];

  assign ds_d       = r_ds;
  assign register_d = r_register;

endmodule


// module decoder_test();
//   reg clk, rstn;

//   reg  [8-1:0] ind;

//   wire [4-1:0] opecode;
//   wire         cflag;
//   reg  [2-1:0] ds;
//   reg  [4-1:0] register;

//   assign opecode = ind[7:4];
//   assign cflag   = ind[3];

//   cpu_decoder cpu_decoder0( .clk(clk) 
//                            ,.rstn(rstn)
//                            ,.opecode(opecode)
//                            ,.cflag(cflag)
//                            ,.ds(ds)
//                            ,.register(register)
//                            );

//   initial begin
//     ind = 'h0;
//     @(posedge rstn);        
    
//     forever begin
//       @(posedge clk); #1;ind = ind + 'h1;
//     end
//   end

//   initial begin
//     clk = 1;
//     forever #5 clk = ~clk;
//   end

//   initial begin
//     rstn = 0;
//     #30 rstn = 1;
//   end

//   initial begin
//     #2600 $finish();
//   end

//   always @(posedge clk) begin
//     $write("[%t] 0x%h : 0x%h, 0x%h, 0x%h, 0x%h \n", $time, ind, opecode, cflag, ds, register);
//   end

//   initial begin
//     $dumpfile("decoder_test.vcd");
//     $dumpvars(0, decoder_test);
//   end

// endmodule



