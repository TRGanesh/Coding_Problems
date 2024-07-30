'''
Link : https://www.hackerrank.com/challenges/one-month-preparation-kit-caesar-cipher-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two
'''

'''
- ASCII 97 is for "a"
- ASCII 65 is for "A"
'''
def caesarCipher(s, k):
    # No Need of Any Map
    # idx_alphabets_map = {}
    # for i in range(26):
    #     alphabet = chr(97 + i)
    #     idx_alphabets_map[i] = alphabet
         
    ans = []
    for idx, char in enumerate(s):
        if "a" <= char <= "z": # Lower Case
            cur_char_ascii = ord(char)
            # Convert to Base Numbering(0-25) -- Subtract with 97
            cur_char_base_ascii = cur_char_ascii - 97
            # Add k
            updated_char_ascii = cur_char_base_ascii + k
            # Do Take Mod with 26 for Circularity
            updated_char_ascii = updated_char_ascii % 26
            # Again do Add 97 for Real Alphabet
            updated_char_ascii = updated_char_ascii + 97
            
            new_char = chr(updated_char_ascii)
            ans.append(new_char)
        elif "A" <= char <= "Z": # Upper Case
            cur_char_ascii = ord(char)
            # Convert to Base(0-25) -- Subtract with 65("A")
            cur_char_base_ascii = cur_char_ascii - 65
            # Add k
            updated_char_ascii = cur_char_base_ascii + k
            # Do Take Mod with 26 for Circularity
            updated_char_ascii = updated_char_ascii % 26
            # Again do Add 65 for Real Alphabet
            updated_char_ascii = updated_char_ascii + 65
            
            new_char = chr(updated_char_ascii)
            ans.append(new_char)
        
        else:
            ans.append(char)
    
    # print(ans)
    return "".join(ans)
