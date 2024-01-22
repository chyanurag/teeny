# <p style="text-align: center;">Teeny</p>
## <p style="text-align: center">A transpiler to convert BASIC like code to C</p>

Variables (For now only ints and floats are supported)  
```
LET a = 4
LET b = 8.278
LET c = a + b
```

Operators (Arithmetic and comparison)
```
LET a = 45
LET b = a * a
LET c = b - a
LET d = c / a
```

Conditionals
```
IF a > 5 THEN
    PRINTLN "A is greater than 5"
ENDIF
```

Looping
```
LET n = 5
LET s = 0
WHILE n > 0 REPEAT
    LET s = s + n
    LET n = n - 1
ENDWHILE
```

Built-ins
```
PRINT "Hi!!"
PRINTLN "Print but with a newline"
PRINTLN 3 + 5
```
Output
```
Hi!!Print but with a newline
8
```
INPUT - takes a number input
```
INPUT n
WHILE n > 5 REPEAT
    PRINT n
    PRINT " "
    LET n = n - 1
ENDWHILE
PRINTLN ""
```

Calling C code
```
LET a = 4
LET b = 5
`
    b = a * a;
    printf("Changed b to %f\n", b);
`
PRINTLN b
```

Comments
```
# This is a comment
PRINTLN "Hello!" # This will be ignored
```

Reference
[Let's make a Teeny Tiny Compiler](https://austinhenley.com/blog/teenytinycompiler1.html)  
A really great 3 part article on how compilers work
