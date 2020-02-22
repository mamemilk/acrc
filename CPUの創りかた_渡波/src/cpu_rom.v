module cpu_rom(
   input          clk
  ,input          rstn
  ,input  [4-1:0] addr
  ,output [8-1:0] data
  ,output [8-1:0] data_d
);

  reg [8-1:0] r_reg;

  //ADD A, Im 0000
  //ADD B, Im 0101
  //MOV A, Im 0011
  //MOV B, Im 0111
  //MOV A, B  0001
  //MOV B, A  0100
  //JMP Im    1111
  //JNC Im    1110
  //IN A      0010
  //IN B      0110
  //OUT B     1001
  //OUT Im    1011

  function [8-1:0] romdata;
    input [4-1:0] addr;
    case(addr)
      0:         romdata = 8'b1011_0111;
      1:         romdata = 8'b0000_0001;
      2:         romdata = 8'b1110_0001;
      3:         romdata = 8'b0000_0001;
      4:         romdata = 8'b1110_0011;
      5:         romdata = 8'b1011_0110;
      6:         romdata = 8'b0000_0001;
      7:         romdata = 8'b1110_0110;
      8:         romdata = 8'b0000_0001;
      9:         romdata = 8'b1110_1000;
      10:        romdata = 8'b1011_0000;
      11:        romdata = 8'b1011_0100;
      12:        romdata = 8'b0000_0001;
      13:        romdata = 8'b1110_1010;
      14:        romdata = 8'b1011_1000;
      15:        romdata = 8'b1111_1111;
      default : romdata = 8'bxxxxxxxx;
    endcase
  endfunction

  always @(negedge rstn or posedge clk)  begin
    if (~rstn)
      r_reg <= #1 8'h0;
    else
      r_reg <= #1 data;
  end

  assign data   = romdata(addr);
  assign data_d = r_reg;

endmodule


// module rom_test();
//   reg clk, rstn;

//   reg [4-1:0] addr;
//   reg [8-1:0] data;

//   cpu_rom cpu_rom0(.clk(clk), .rstn(rstn), .addr(addr), .data(data));

//   initial begin
//     addr = 'h0;
//     @(posedge rstn);        
    
//     repeat(16) begin
//       @(posedge clk); #1;addr = addr + 'h1;
//     end
//   end

//   initial begin
//     clk = 0;
//     forever #10 clk = ~clk;
//   end

//   initial begin
//     rstn = 0;
//     #30 rstn = 1;
//   end

//   initial begin
//     #500 $finish();
//   end

//   always @(posedge clk) begin
//     $write("[%t] 0x%h, 0x%h \n", $time, addr, data);
//   end

//   initial begin
//       $dumpfile("rom_test.vcd");
//       $dumpvars(0, rom_test);
//   end

// endmodule



