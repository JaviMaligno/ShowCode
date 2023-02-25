class Bataille:
    values = {"2":0, "3":1, "4":2, "5":3, "6":4, "7":5, "8":6, "9":7, "T":8, "J":9, "Q":10, "K":11, "A":12}
    def play(self, player1_deck, player2_deck):
        # Your code goes here
        if not player1_deck and not player2_deck:
            return 0 
        if not player2_deck:
            return 1 
        if not player1_deck:
            return 2 
            
        down_deck_1 = player1_deck
        down_deck_2 = player2_deck
        up_deck_1 = ""
        up_deck_2 = ""
        war_deck_1 = ""
        war_deck_2 = ""

        while True:
            if not any([down_deck_1, up_deck_1, down_deck_2, up_deck_2]):
                return 0 
            if down_deck_1:
                    war_deck_1 = down_deck_1[0] + war_deck_1 
                    down_deck_1 = down_deck_1[1:]
            elif up_deck_1:
                    down_deck_1 = up_deck_1[::-1]
                    up_deck_1 = ""
                    war_deck_1 = down_deck_1[0] + war_deck_1 
                    down_deck_1 = down_deck_1[1:]
            else:
                    return 2 
                
            if down_deck_2:
                    war_deck_2 = down_deck_2[0] + war_deck_2 
                    down_deck_2 = down_deck_2[1:]
            elif up_deck_2:
                    down_deck_2 = up_deck_2[::-1]
                    up_deck_2 = ""
                    war_deck_2 = down_deck_2[0] + war_deck_2 
                    down_deck_2 = down_deck_2[1:]
            else:
                    return 1 
                    
         
            if self.values[war_deck_1[0]] > self.values[war_deck_2[0]]:
                up_deck_1 = war_deck_1 + war_deck_2 + up_deck_1
                war_deck_1 = ""
                war_deck_2 = ""
            elif self.values[war_deck_1[0]] < self.values[war_deck_2[0]]:
                up_deck_2 = war_deck_2 + war_deck_1 + up_deck_2
                war_deck_1 = ""
                war_deck_2 = ""
            else:
                if not any([down_deck_1, up_deck_1, down_deck_2, up_deck_2]):
                    return 0 
                if down_deck_1:
                    war_deck_1 = down_deck_1[0] + war_deck_1 
                    down_deck_1 = down_deck_1[1:]
                elif up_deck_1:
                    down_deck_1 = up_deck_1[::-1]
                    up_deck_1 = ""
                    war_deck_1 = down_deck_1[0] + war_deck_1 
                    down_deck_1 = down_deck_1[1:]
                else:
                    return 2 
                
                if down_deck_2:
                    war_deck_2 = down_deck_2[0] + war_deck_2 
                    down_deck_2 = down_deck_2[1:]
                elif up_deck_2:
                    down_deck_2 = up_deck_2[::-1]
                    up_deck_2 = ""
                    war_deck_2 = down_deck_2[0] + war_deck_2 
                    down_deck_2 = down_deck_2[1:]
                else:
                    return 1 
                
