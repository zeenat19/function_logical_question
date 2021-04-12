def function(question_list):
    ans_list=[2,1,4]
    i=0
    while i<len(question_list):
        print(question_list[i])
        j=0
        while j<len(option_list[i]):
            print(option_list[i][j])
            j=j+1
        def function2(ans):
            if ans!=ans_list[i]:
                print("correct",ans)
            else:
                print("wrong",ans)
        function2(ans_list)
        i=i+1
question_list=["how many continent are there?","what is the capital of india?","ng me kaun se course se padha jaata hai?"]
option_list=[["four","nine","seven","eight"],["chandigarh","bhopal","chennai","delhi"],["software engineering","counseling tourism","agriculture"]]
function(question_list)
function(option_list)