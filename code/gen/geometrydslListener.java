// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link geometrydslParser}.
 */
public interface geometrydslListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(geometrydslParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(geometrydslParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#variableDeclarations}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclarations(geometrydslParser.VariableDeclarationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#variableDeclarations}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclarations(geometrydslParser.VariableDeclarationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#variableDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclaration(geometrydslParser.VariableDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#variableDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclaration(geometrydslParser.VariableDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(geometrydslParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(geometrydslParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(geometrydslParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(geometrydslParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#methodInvocations}.
	 * @param ctx the parse tree
	 */
	void enterMethodInvocations(geometrydslParser.MethodInvocationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#methodInvocations}.
	 * @param ctx the parse tree
	 */
	void exitMethodInvocations(geometrydslParser.MethodInvocationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#methodInvocation}.
	 * @param ctx the parse tree
	 */
	void enterMethodInvocation(geometrydslParser.MethodInvocationContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#methodInvocation}.
	 * @param ctx the parse tree
	 */
	void exitMethodInvocation(geometrydslParser.MethodInvocationContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#methodName}.
	 * @param ctx the parse tree
	 */
	void enterMethodName(geometrydslParser.MethodNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#methodName}.
	 * @param ctx the parse tree
	 */
	void exitMethodName(geometrydslParser.MethodNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(geometrydslParser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(geometrydslParser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(geometrydslParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(geometrydslParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#numericType}.
	 * @param ctx the parse tree
	 */
	void enterNumericType(geometrydslParser.NumericTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#numericType}.
	 * @param ctx the parse tree
	 */
	void exitNumericType(geometrydslParser.NumericTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#floatingPoint}.
	 * @param ctx the parse tree
	 */
	void enterFloatingPoint(geometrydslParser.FloatingPointContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#floatingPoint}.
	 * @param ctx the parse tree
	 */
	void exitFloatingPoint(geometrydslParser.FloatingPointContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#decimalNumeral}.
	 * @param ctx the parse tree
	 */
	void enterDecimalNumeral(geometrydslParser.DecimalNumeralContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#decimalNumeral}.
	 * @param ctx the parse tree
	 */
	void exitDecimalNumeral(geometrydslParser.DecimalNumeralContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#stringLiteral}.
	 * @param ctx the parse tree
	 */
	void enterStringLiteral(geometrydslParser.StringLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#stringLiteral}.
	 * @param ctx the parse tree
	 */
	void exitStringLiteral(geometrydslParser.StringLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#stringCharacters}.
	 * @param ctx the parse tree
	 */
	void enterStringCharacters(geometrydslParser.StringCharactersContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#stringCharacters}.
	 * @param ctx the parse tree
	 */
	void exitStringCharacters(geometrydslParser.StringCharactersContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void enterBooleanLiteral(geometrydslParser.BooleanLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#booleanLiteral}.
	 * @param ctx the parse tree
	 */
	void exitBooleanLiteral(geometrydslParser.BooleanLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#comments}.
	 * @param ctx the parse tree
	 */
	void enterComments(geometrydslParser.CommentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#comments}.
	 * @param ctx the parse tree
	 */
	void exitComments(geometrydslParser.CommentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link geometrydslParser#comment}.
	 * @param ctx the parse tree
	 */
	void enterComment(geometrydslParser.CommentContext ctx);
	/**
	 * Exit a parse tree produced by {@link geometrydslParser#comment}.
	 * @param ctx the parse tree
	 */
	void exitComment(geometrydslParser.CommentContext ctx);
}