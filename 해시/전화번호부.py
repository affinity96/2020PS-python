def solution(phone_book):
    length = len(phone_book)
    #전화번호부를 전화번호의 길이와 함께 딕셔너리화
    phone_book_with_len = {phone : len(phone) for i, phone in enumerate(phone_book)}
    #딕셔너리를 전화번호의 길이에 따라 정렬
    phone_book_with_len = sorted(phone_book_with_len.items(), key = lambda x:x[1])
    
    #하나씩 탐색. 비교하고자 하는 대상의 0부터 타겟의 길이까지가 타겟과 같으면 접두사
    for i, (phone_num, phone_len) in enumerate(phone_book_with_len):
    #끝까지 탐색한다면 더이상 접두사가 될 수 없음
        if i == length-1 : return True
        for j, (phone_num_vs, phone_len_vs) in enumerate(phone_book_with_len[i+1:]):
            if phone_num == phone_num_vs[:phone_len] : return False
