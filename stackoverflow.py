def question_posted(down_votes,up_votes):
  down_points = down_votes * (-2)
  up_points = up_votes * 10
  return down_points + up_points


def answers(accept,down_votes,up_votes):
  if accept == 'accepted':
    accepted_points = 15
  else:
    accepted_points = 0
  down_points = down_votes * (-2)
  up_points = up_votes * 10
  return accepted_points + down_points + up_points 


def main():
  questions =[[5,2],
             [0,10]
             ]
  answers_list =[['accepted',0,0],
                ['accepted',0,10],
                ['not accepted',2,3]
                ]
  total = 0
  for i in questions:
    total += question_posted(i[0],i[1])
  for i in answers_list:
    total += answers(i[0],i[1],i[2])
  print(total)  

if __name__ == "__main__":
  main()
