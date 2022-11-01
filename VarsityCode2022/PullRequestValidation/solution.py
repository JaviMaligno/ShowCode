class Solution:

    def verifypr(self, PR):
        # Your code goes here
        if not PR:
            return False
        
        commits = list(map(lambda x: x.split(','), PR))
        if any(len(x) != 4 for x in commits):
            return False
            
        sn_list = []    
        
        return all(self.check_sn(commit, sn_list) and self.check_msg(commit) and self.check_hash(commit) for commit in commits )

    @staticmethod            
    def check_sn(commit, sn_list):
        try:
            sn = int(commit[0],16)
            if sn_list:
                pc = sn_list[-1]
                if sn-pc != 1:
                    return False
                else:
                    sn_list.append(sn)
            else:
                sn_list.append(sn)
        except ValueError:
            return False
        return True
    
    def check_msg(self, commit):
        msg = commit[1].split('-')
        l = len(msg)
        if l < 3:
            return False
        elif l == 3:
            ticket = msg[0]
            c_type = msg[1]
            code = msg[2]
            return self.check_ticket(ticket) and self.check_type(c_type) and self.check_code(code)
        else:
            if not msg[0]:
                ticket = '-'+msg[1]
                c_type = msg[2]
                code = msg[3:]
                return self.check_ticket(ticket, negative = True) and self.check_type(c_type) and self.check_code(code)
            else:
                ticket = msg[0]
                c_type = msg[1]
                code = msg[2:]
                
                return self.check_ticket(ticket) and self.check_type(c_type) and self.check_code(code)

    @staticmethod
    def check_ticket(ticket, negative = False):
        try:
            ticket_n = int(ticket)
            l = len(ticket)
            return l == 5 if negative else l == 4
        except ValueError:
            return False
            
    @staticmethod
    def check_type(c_type):
        types = ['fix', 'feat', 'chore', 'refactor']
        return c_type in types
        
    @staticmethod
    def check_code(code):
        return bool(code)
        
    @staticmethod
    def check_hash(commit):
        try:
            file = commit[2]
            file_value = int(file)
            h_value = commit[3]
            r = file_value % 151
            correct_hash = str(r)[::-1]
            return h_value == correct_hash
        except ValueError:
            return False