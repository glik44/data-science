
def brainfuck(input):
    data = [0 for i in range(100)]
    cur_data_index = 0
    cur_input_index = 0
    loop_stack = []
    output = []

    while cur_input_index < len(input):
        if input[cur_input_index] == '+':
            data[cur_data_index] += 1

        elif input[cur_input_index] == '-':
            data[cur_data_index] -= 1

        elif input[cur_input_index] == '>' :
            cur_data_index += 1

        elif input[cur_input_index] == '<':
            cur_data_index -= 1

        elif input[cur_input_index] == '.':
            output.append(chr(data[cur_data_index]))

        elif input[cur_input_index] == ',':
            continue;

        elif input[cur_input_index] == '[':
            loop_stack.append(cur_input_index - 1)
            if data[cur_data_index] == 0:
                while input[cur_input_index] != ']':
                    cur_input_index += 1

        elif input[cur_input_index] == ']':
            index = loop_stack.pop()
            if data[cur_data_index] != 0:
                cur_input_index = index

        else:
            return "ERROR in index: " + str(cur_input_index)

        cur_input_index += 1

    return " ".join(output)

if __name__ == '__main__':
    input = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
    res = brainfuck(input)
    print(res)