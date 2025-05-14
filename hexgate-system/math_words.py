import numpy as np

class MathWords:
    @staticmethod
    def register(vm):

        # Increment by 1
        vm.define('inc', lambda: MathWords._inc(vm))

        # Multiplication: a b * → a*b
        vm.define('*', lambda: vm.stack.append(np.float64(vm.stack.pop()) * np.float64(vm.stack.pop())))

        # Division: b a / → a/b
        vm.define('/', lambda: MathWords._safe_divide(vm))

        # Modulus: b a mod → a % b
        vm.define('mod', lambda: MathWords._safe_mod(vm))

        # Negation: a neg → -a
        vm.define('neg', lambda: vm.stack.append(-np.float64(vm.stack.pop())))

        # Absolute value: a abs → |a|
        vm.define('abs', lambda: vm.stack.append(np.abs(vm.stack.pop())))

        # Minimum: a b min → min(a, b)
        vm.define('min', lambda: MathWords._binary_op(vm, np.minimum))

        # Maximum: a b max → max(a, b)
        vm.define('max', lambda: MathWords._binary_op(vm, np.maximum))

        # Clamp: min max val clamp → clamped value
        vm.define('clamp', lambda: MathWords._clamp(vm))

        # Power: b a pow → a^b
        vm.define('pow', lambda: MathWords._binary_op(vm, np.power))

        # Square root: a sqrt → √a
        vm.define('sqrt', lambda: MathWords._sqrt(vm))

    @staticmethod
    def _binary_op(vm, func):
        b = np.float64(vm.stack.pop())
        a = np.float64(vm.stack.pop())
        vm.stack.append(func(a, b))

    @staticmethod
    def _inc(vm):
        a = np.float64(vm.stack.pop())
        vm.stack.append(a + 1)

    @staticmethod
    def _safe_divide(vm):
        b = np.float64(vm.stack.pop())
        a = np.float64(vm.stack.pop())
        if b == 0:
            raise ZeroDivisionError("Division by zero.")
        vm.stack.append(a / b)

    @staticmethod
    def _safe_mod(vm):
        b = np.float64(vm.stack.pop())
        a = np.float64(vm.stack.pop())
        if b == 0:
            raise ZeroDivisionError("Modulo by zero.")
        vm.stack.append(np.mod(a, b))

    @staticmethod
    def _clamp(vm):
        val = np.float64(vm.stack.pop())
        max_val = np.float64(vm.stack.pop())
        min_val = np.float64(vm.stack.pop())
        vm.stack.append(np.clip(val, min_val, max_val))

    @staticmethod
    def _sqrt(vm):
        a = np.float64(vm.stack.pop())
        if a < 0:
            raise ValueError("Cannot take square root of negative number.")
        vm.stack.append(np.sqrt(a))
