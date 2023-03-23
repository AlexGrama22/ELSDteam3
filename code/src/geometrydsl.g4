grammar geometrydsl;

start: 'START'* variableDeclarations? methodInvocations? comments? 'END';

variableDeclarations: variableDeclaration | variableDeclarations variableDeclaration;
variableDeclaration: type identifier;

type: 'Point' | 'Line' | 'Segment' | 'Triangle' | 'Square' | 'Rectangle' | 'Parallelogram' | 'Trapezoid' | 'Rhombus' | 'Circle' | 'Ellipse' | 'Cube' | 'Sphere' | 'Cylinder' | 'Cone';

identifier: (LETTER | '_') (LETTER | DIGIT | '_')*;

methodInvocations: methodInvocation | methodInvocations methodInvocation;
methodInvocation: identifier '.' methodName '(' argumentList? ')';
methodName: 'length' | 'angle' | 'radius' | 'diagonal' | 'median' | 'bisector' | 'vertex_name' | 'angle_name' | 'area' | 'perimeter' | 'volume' | 'setParameters';

argumentList: expression | argumentList ',' expression;
expression: numericType | stringLiteral | booleanLiteral;

numericType: decimalNumeral | floatingPoint;
floatingPoint: decimalNumeral '.' decimalNumeral;
decimalNumeral: DIGIT+;

stringLiteral: '"' stringCharacters? '"';
stringCharacters: (LETTER | DIGIT)*;

booleanLiteral: 'true' | 'false';

comments: comment | comments comment;
comment: '//' stringLiteral;

LETTER: [a-zA-Z];
DIGIT: [0-9];

WS: [ \t\n\r] -> skip;
