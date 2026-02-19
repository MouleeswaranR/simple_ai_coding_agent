# calculator.py

import sys
from pkg.calculator import add, subtract, multiply, divide
from pkg.render import show_result, show_error

# --------------------------------------------------------------------
# Operator definitions with precedence and lambda functions
# --------------------------------------------------------------------

PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '%': 2,
}

OPERATIONS = {
    '+': lambda a, b: add(a, b),
    '-': lambda a, b: subtract(a, b),
    '*': lambda a, b: multiply(a, b),
    '/': lambda a, b: divide(a, b),
    '%': lambda a, b: divide(a, b),
}


def tokenize(expression: str) -> list:
    """Step 1: Convert raw string into list of tokens (numbers and operators)"""
    print("\n[DEBUG] Step 1: Tokenizing the input expression")
    print(f"   Original input: {expression!r}")

    # Remove all whitespace (spaces, tabs)
    cleaned = expression.replace(" ", "").replace("\t", "")
    print(f"   After removing whitespace: {cleaned!r}")

    tokens = []
    i = 0
    while i < len(cleaned):
        char = cleaned[i]

        # Number detection (integer or decimal)
        if char.isdigit() or char == '.':
            num_str = ''
            while i < len(cleaned) and (cleaned[i].isdigit() or cleaned[i] == '.'):
                num_str += cleaned[i]
                i += 1
            num_value = float(num_str)
            tokens.append(num_value)
            print(f"   -> Found number: {num_str} -> {num_value}")
            continue

        # Operator or parenthesis
        if char in '+-*/%()':
            tokens.append(char)
            print(f"   -> Found operator/parenthesis: {char}")
        else:
            raise ValueError(f"Invalid character found: '{char}'")

        i += 1

    print(f"   Final tokens: {tokens}\n")
    return tokens


def infix_to_postfix(tokens: list) -> list:
    """Step 2: Convert infix -> postfix (Reverse Polish Notation) using precedence"""
    print("[DEBUG] Step 2: Converting to postfix (RPN) using operator precedence")
    print(f"   Input tokens: {tokens}")

    output = []
    operators = []

    for token in tokens:
        if isinstance(token, float):
            output.append(token)
            print(f"   -> Number to output: {token}")
        elif token == '(':
            operators.append(token)
            print(f"   -> Push '(' to operators stack")
        elif token == ')':
            print(f"   -> Closing ')', popping operators until '('")
            while operators and operators[-1] != '(':
                popped = operators.pop()
                output.append(popped)
                print(f"      Popped {popped} -> output")
            if not operators:
                raise ValueError("Mismatched parentheses")
            operators.pop()  # remove '('
            print(f"   -> Removed '(' from stack")
        elif token in PRECEDENCE:
            print(f"   -> Operator {token} (precedence {PRECEDENCE[token]})")
            while (operators and operators[-1] != '(' and
                   PRECEDENCE.get(operators[-1], 0) >= PRECEDENCE[token]):
                popped = operators.pop()
                output.append(popped)
                print(f"      Higher/equal precedence -> pop {popped} -> output")
            operators.append(token)
            print(f"      Push {token} to operators")
        else:
            raise ValueError(f"Unknown token: {token}")

    # Empty remaining operators
    while operators:
        if operators[-1] == '(':
            raise ValueError("Mismatched parentheses")
        popped = operators.pop()
        output.append(popped)
        print(f"   -> Remaining operator popped: {popped} -> output")

    print(f"   Final postfix: {output}\n")
    return output


def evaluate_postfix(postfix: list) -> float:
    """Step 3: Evaluate postfix expression using stack and lambda functions"""
    print("[DEBUG] Step 3: Evaluating postfix expression")
    print(f"   Postfix: {postfix}")

    stack = []

    for token in postfix:
        if isinstance(token, float):
            stack.append(token)
            print(f"   -> Push number to stack: {token}   stack = {stack}")
        elif token in OPERATIONS:
            if len(stack) < 2:
                raise ValueError("Invalid expression - not enough operands")
            b = stack.pop()
            a = stack.pop()
            print(f"   -> Operator {token}:  {a} {token} {b}")
            try:
                result = OPERATIONS[token](a, b)
                stack.append(result)
                print(f"      Result: {result}   stack = {stack}")
            except ValueError as e:
                raise e
        else:
            raise ValueError(f"Unknown operator: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid expression - too many operands")
    
    final_result = stack[0]
    print(f"   Final result: {final_result}\n")
    return final_result


def calculate(expression: str) -> float:
    """Main calculation pipeline with debug prints"""
    print("=" * 70)
    print(f"Calculating expression: {expression!r}")
    print("=" * 70)

    tokens = tokenize(expression)
    postfix = infix_to_postfix(tokens)
    result = evaluate_postfix(postfix)

    print("-" * 70)
    return result


def main():
    # --- Command-line mode with detailed explanation ----------
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])

        try:
            result = calculate(expr)
            # Clean output for automation
            if result.is_integer():
                print(int(result))
            else:
                print(result)
            sys.exit(0)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}", file=sys.stderr)
            sys.exit(1)

    # --- Interactive mode (no debug prints) -------------------
    print("Calculator with precedence  (Ctrl+C or 'q' to quit)")
    print("Examples:")
    print("  2 + 3 * 4     -> 14")
    print("  10 - 6 / 2    -> 7")
    print("  (5 + 3) * 2    -> 16\n")

    while True:
        try:
            line = input("> ").strip()
            if not line:
                continue
            if line.lower() in ('q', 'quit', 'exit'):
                print("Goodbye.")
                break

            result = calculate(line)  # still uses debug prints
            print(f"  {line}  =  {int(result) if result.is_integer() else result}")

        except ValueError as e:
            show_error(str(e))
        except KeyboardInterrupt:
            print("\nGoodbye.")
            sys.exit(0)
        except Exception as e:
            show_error(f"unexpected error: {e}")


if __name__ == "__main__":
    main()