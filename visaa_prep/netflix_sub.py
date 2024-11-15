vignesh_amt, charan_amt, rishi_amt, netflix_cost = map(int, input().split())
if(vignesh_amt + charan_amt >= netflix_cost) or (vignesh_amt + rishi_amt >= netflix_cost) or (charan_amt + rishi_amt >= netflix_cost):
    print("YES")
else:
    print("NO")
