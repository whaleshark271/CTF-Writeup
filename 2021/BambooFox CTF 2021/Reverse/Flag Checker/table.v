module magic(
  input clk,
  input rst,
  input[7:0] inp,
  input[1:0] val,
  output reg[7:0] res
);
  always @(*) begin
    case (val)
      2'b00: res = (inp >> 3) | (inp << 5);
      2'b01: res = (inp << 2) | (inp >> 6);
      2'b10: res = inp + 8'b110111;
      2'b11: res = inp ^ 8'd55;
    endcase
  end
endmodule

module chall(
  input clk,
  input rst,
  input[7:0] inp,
  output reg[7:0] res
);
  wire[1:0] val0 = inp[1:0];
  wire[1:0] val1 = inp[3:2];
  wire[1:0] val2 = inp[5:4];
  wire[1:0] val3 = inp[7:6];
  wire[7:0] res0, res1, res2, res3;

  magic m0(.clk(clk), .rst(rst), .inp(inp), .val(val0), .res(res0));
  magic m1(.clk(clk), .rst(rst), .inp(res0), .val(val1), .res(res1));
  magic m2(.clk(clk), .rst(rst), .inp(res1), .val(val2), .res(res2));
  magic m3(.clk(clk), .rst(rst), .inp(res2), .val(val3), .res(res3));

  always @(posedge clk) begin
    if (rst) begin
      assign res = inp;
    end else begin
      assign res = res3;
    end
  end
endmodule

module main;
    reg clk, rst, ok;
    reg[7:0] inp, idx, tmp;
    reg[7:0] res[32:0];
    wire[7:0] out;
    wire[7:0] flag[64:0];

    // change the content of the flag as you need
    // 0~9
    assign flag[0] = 48;
    assign flag[1] = 49;
    assign flag[2] = 50;
    assign flag[3] = 51;
    assign flag[4] = 52;
    assign flag[5] = 53;
    assign flag[6] = 54;
    assign flag[7] = 55;
    assign flag[8] = 56;
    assign flag[9] = 57;
    // _
    assign flag[10] = 95;
    // A~Z
    assign flag[11] = 65;
    assign flag[12] = 66;
    assign flag[13] = 67;
    assign flag[14] = 68;
    assign flag[15] = 69;
    assign flag[16] = 70;
    assign flag[17] = 71;
    assign flag[18] = 72;
    assign flag[19] = 73;
    assign flag[20] = 74;
    assign flag[21] = 75;
    assign flag[22] = 76;
    assign flag[23] = 77;
    assign flag[24] = 78;
    assign flag[25] = 79;
    assign flag[26] = 80;
    assign flag[27] = 81;
    assign flag[28] = 82;
    assign flag[29] = 83;
    assign flag[30] = 84;
    assign flag[31] = 85;
    assign flag[32] = 86;
    assign flag[33] = 87;
    assign flag[34] = 88;
    assign flag[35] = 89;
    assign flag[36] = 90;
    //a~z
    assign flag[37] = 97;
    assign flag[38] = 98;
    assign flag[39] = 99;
    assign flag[40] = 100;
    assign flag[41] = 101;
    assign flag[42] = 102;
    assign flag[43] = 103;
    assign flag[44] = 104;
    assign flag[45] = 105;
    assign flag[46] = 106;
    assign flag[47] = 107;
    assign flag[48] = 108;
    assign flag[49] = 109;
    assign flag[50] = 110;
    assign flag[51] = 111;
    assign flag[52] = 112;
    assign flag[53] = 113;
    assign flag[54] = 114;
    assign flag[55] = 115;
    assign flag[56] = 116;
    assign flag[57] = 117;
    assign flag[58] = 118;
    assign flag[59] = 119;
    assign flag[60] = 120;
    assign flag[61] = 121;
    assign flag[62] = 122;
    //!
    assign flag[63] = 33;

    chall ch(.clk(clk), .rst(rst), .inp(inp), .res(out));

    initial begin
        $dumpfile("chall.vcd");
        $dumpvars;

        clk = 1'b0;
        #1 rst = 1'b1;
        #1 rst = 1'b0;
        inp = flag[0];

        for (idx = 0; idx < 64; idx++) begin
            inp = flag[idx];
            #4;
        end

        $finish;
    end

    always @(posedge clk) begin
        #1 $display("%c %d", flag[idx], out);
    end

    always begin
        #2 clk = ~clk;
    end
endmodule