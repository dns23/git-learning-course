class Fibonacci:

    def getTerms(self, terms = 10):
        f1 = 1
        f2 = 1
        if terms < 1:
            return []
        elif terms == 1:
            return [f1]
        elif terms == 2:
            return [f1, f2]
        else:
            results = []
            results.append(f1)
            results.append(f2)
            term = 3
            while (term <= terms):
                tmp = f2 + f1
                results.append(tmp)
                f2 = f1
                f1 = tmp
                term += 1
            return results
