from collections import defaultdict
def solution(genres, plays):
    music_dic = defaultdict(lambda : [])
    answer = []
    genre_count = defaultdict(lambda : 0)
    music_list= list(enumerate(zip(genres, plays)))
    music_list.sort(reverse=True, key = lambda x : x[1][1])
    for (i, (genre,play)) in music_list:
        genre_count[genre] += play
        music_dic[genre].append(i)
    genre_count = sorted(genre_count.items(), key = lambda x : x[1], reverse = True)

    for (genre,play) in genre_count:
        

        if len(music_dic[genre]) == 1 : answer.append(music_dic[genre][0])
        else : 
            answer.append(music_dic[genre][0])
            answer.append(music_dic[genre][1])
    return answer
