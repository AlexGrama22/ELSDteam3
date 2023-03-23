// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link geometrydslParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface geometrydslVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#start}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStart(geometrydslParser.StartContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#variableDeclarations}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariableDeclarations(geometrydslParser.VariableDeclarationsContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#variableDeclaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariableDeclaration(geometrydslParser.VariableDeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType(geometrydslParser.TypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#identifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdentifier(geometrydslParser.IdentifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#methodInvocations}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethodInvocations(geometrydslParser.MethodInvocationsContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#methodInvocation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethodInvocation(geometrydslParser.MethodInvocationContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#methodName}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethodName(geometrydslParser.MethodNameContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#argumentList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgumentList(geometrydslParser.ArgumentListContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(geometrydslParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#numericType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNumericType(geometrydslParser.NumericTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#floatingPoint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFloatingPoint(geometrydslParser.FloatingPointContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#decimalNumeral}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDecimalNumeral(geometrydslParser.DecimalNumeralContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#stringLiteral}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStringLiteral(geometrydslParser.StringLiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#stringCharacters}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStringCharacters(geometrydslParser.StringCharactersContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#booleanLiteral}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBooleanLiteral(geometrydslParser.BooleanLiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#comments}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComments(geometrydslParser.CommentsContext ctx);
	/**
	 * Visit a parse tree produced by {@link geometrydslParser#comment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComment(geometrydslParser.CommentContext ctx);
}