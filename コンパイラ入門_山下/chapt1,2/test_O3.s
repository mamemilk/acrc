	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 15	sdk_version 10, 15
	.section	__TEXT,__literal8,8byte_literals
	.p2align	3               ## -- Begin function main
LCPI0_0:
	.quad	4607182418800017408     ## double 1
LCPI0_1:
	.quad	4613937818241073152     ## double 3
LCPI0_2:
	.quad	4618441417868443648     ## double 6
LCPI0_3:
	.quad	4621819117588971520     ## double 10
LCPI0_4:
	.quad	4624633867356078080     ## double 15
LCPI0_5:
	.quad	4626604192193052672     ## double 21
LCPI0_6:
	.quad	4628574517030027264     ## double 28
LCPI0_7:
	.quad	4630263366890291200     ## double 36
LCPI0_8:
	.quad	4631530004285489152     ## double 45
LCPI0_9:
	.quad	4632937379169042432     ## double 55
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	pushq	%rbx
	pushq	%rax
	.cfi_offset %rbx, -24
	leaq	L_.str(%rip), %rbx
	xorps	%xmm0, %xmm0
	movq	%rbx, %rdi
	movb	$1, %al
	callq	_printf
	movsd	LCPI0_0(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	%rbx, %rdi
	movb	$1, %al
	callq	_printf
	movsd	LCPI0_1(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	%rbx, %rdi
	movb	$1, %al
	callq	_printf
	movsd	LCPI0_2(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	%rbx, %rdi
	movb	$1, %al
	callq	_printf
	movsd	LCPI0_3(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	%rbx, %rdi
	movb	$1, %al
	callq	_printf
	movsd	LCPI0_4(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	%rbx, %rdi
	movb	$1, %al
	callq	_printf
	movsd	LCPI0_5(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	%rbx, %rdi
	movb	$1, %al
	callq	_printf
	movsd	LCPI0_6(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	%rbx, %rdi
	movb	$1, %al
	callq	_printf
	movsd	LCPI0_7(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	%rbx, %rdi
	movb	$1, %al
	callq	_printf
	movsd	LCPI0_8(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	%rbx, %rdi
	movb	$1, %al
	callq	_printf
	movsd	LCPI0_9(%rip), %xmm0    ## xmm0 = mem[0],zero
	movq	%rbx, %rdi
	movb	$1, %al
	callq	_printf
	xorl	%eax, %eax
	addq	$8, %rsp
	popq	%rbx
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"%f\n"


.subsections_via_symbols
