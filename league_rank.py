import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   # Get command line arguments and show required usage if there is an error
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["input_file=","output_file="])
   except getopt.GetoptError:
      print('league_rank.py -i <inputfile> -o <outputfile>')
      # using sys.exit arg 2 - interpreted by UNIX as command line syntax error
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('league_rank.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--input_file"):
         inputfile = arg
      elif opt in ("-o", "--output_file"):
         outputfile = arg

   #Get results from input file: assumption: all inputs are well-formed, including no extra spaces except for trailing whitespace
   with open(inputfile, "r") as raw_input:
      raw_results = raw_input.readlines()
      raw_results = [row.rstrip() for row in raw_results]

   score_dict = {}
   results = list(map(lambda result: tuple(result.split(", ")), raw_results))

   for i in range(0, len(results)):
      next_result_team1 = results[i][0].rsplit(" ", 1)
      next_result_team2 = results[i][1].rsplit(" ", 1)

      if not (next_result_team1[0] in score_dict):
         score_dict[next_result_team1[0]] = 0;
      if not (next_result_team2[0] in score_dict):
         score_dict[next_result_team2[0]] = 0;

      if int(next_result_team1[1]) > int(next_result_team2[1]):
         score_dict[next_result_team1[0]] += 3
      elif int(next_result_team1[1]) == int(next_result_team2[1]):
         score_dict[next_result_team1[0]] += 1
         score_dict[next_result_team2[0]] += 1
      else:
         score_dict[next_result_team2[0]] += 3

   score_items = list(score_dict.items())
   # ascending sort on negative score allows simultaneous ascending sort on team name for score ties
   score_items.sort(key = lambda x: (-x[1],x[0]))
   with open(outputfile, "w") as outputfile_object:
      placement = 0
      prev_placement = 0
      for i in range(len(score_items)):
         if i == 0 or score_items[i][1] < score_items[i - 1][1]:
            placement = i + 1
            prev_placement = placement
         else:
            placement = prev_placement
         outputfile_object.write(str(placement)+". " + score_items[i][0] + ", " + str(score_items[i][1]) + " pts\n" )


if __name__ == "__main__":
   main(sys.argv[1:])