class main:

    def find_password(self, hidden):
        # Your code goes here
        index = 3
        step = 1
        password = ''
        length = len(hidden)
        if length <= 3:
            return password
        password += hidden[index]
        index +=step
        while length > index:
            password+=hidden[index]
            step*=2
            index +=step
        return password