class SkeletonKey:
    def __init__(self):
        self.stack = []
        self.return_stack = []
        self.dictionary = {}

        # Core instructions
        self.define('+', self._add)
        self.define('-', self._sub)
        self.define('.', self._print)
        self.define('>r', self._to_return_stack)
        self.define('r>', self._from_return_stack)
        self.define('r@', self._peek_return_stack)
        self.define('dup', self._dup)
        self.define(':', self._define_word)

    def define(self, name, func):
        self.dictionary[name] = func

    def _add(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    def _sub(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)

    def _print(self):
        value = self.stack.pop()
        print(value)

    def _to_return_stack(self):
        self.return_stack.append(self.stack.pop())

    def _from_return_stack(self):
        self.stack.append(self.return_stack.pop())

    def _peek_return_stack(self):
        self.stack.append(self.return_stack[-1])

    def _dup(self):
        self.stack.append(self.stack[-1])

    def _define_word(self, tokens, i):
        name = tokens[i + 1]
        body = []
        i += 2
        while i < len(tokens) and tokens[i] != ';':
            body.append(tokens[i])
            i += 1
        self.dictionary[name] = lambda: self.execute(body)
        return i

    def execute(self, tokens):
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.startswith('"') and token.endswith('"'):
                self.stack.append(token.strip('"'))
            elif token.replace('.', '', 1).isdigit():
                self.stack.append(float(token) if '.' in token else int(token))
            elif token in self.dictionary:
                result = self.dictionary[token]
                if callable(result):
                    maybe_new_i = result(tokens, i) if token == ':' else result()
                    if isinstance(maybe_new_i, int):
                        i = maybe_new_i
                else:
                    raise ValueError(f"{token} is not callable.")
            else:
                raise ValueError(f"Unknown word: {token}")
            i += 1

    def run(self, code):
        tokens = code.strip().split()
        self.execute(tokens)
