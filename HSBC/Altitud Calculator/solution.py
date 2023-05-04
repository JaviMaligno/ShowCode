class main:

    def altitude_change(self, values):
        # Your code goes here
        positive = list(filter(lambda x: x>0, values))
        if not positive:
            return [0,0]
        difference = [positive[0]]
        increase = 0
        decrease = 0
        for i in range(1,len(positive)):
            last = difference[-1]
            diff = positive[i] - last
            if -5<= diff <0:
                decrease+=diff
                difference.append(positive[i])
            elif 0<= diff <= 5:
                increase+=diff
                difference.append(positive[i])
            else:
                continue
        return [increase, decrease]