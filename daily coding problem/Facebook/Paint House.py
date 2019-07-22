"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost
to build the nth house with kth color, return the minimum cost which achieves this goal.
"""

def get_costs(N,K):
    paint_house_matrix=[]
    for i in range(N):
        house_color_cost=[]
        for j in range(K):
            house_color_cost.append(int(input("Enter the costs for house "+str(i)+" being painted with color "+str(j)+": ")))    
        paint_house_matrix.append(house_color_cost)
    return paint_house_matrix
            
    
def find_Min_Cost(N,K):

    paint_house_matrix=[[0]*N]*K
    paint_house_matrix=get_costs(N,K)
    if K>=2:
        cost1=0
        cost2=1
        cost1,cost2=(cost1,cost2) if paint_house_matrix[0][cost1]<=paint_house_matrix[0][cost2] else (cost2,cost1)
        for j in range(2,K):
            if paint_house_matrix[0][j]<paint_house_matrix[0][cost1]:
                cost2=cost1
                cost1=j
            elif paint_house_matrix[0][j]<paint_house_matrix[0][cost2]:
                cost2=j

        for i in range(1,N):
            for j in range(K):
                if j!=cost1:
                    paint_house_matrix[i][j]+=paint_house_matrix[i-1][cost1]
                else:
                    paint_house_matrix[i][j]+=paint_house_matrix[i-1][cost2]
            cost1=0
            cost2=1
            cost1,cost2=(cost1,cost2) if paint_house_matrix[i][cost1]<=paint_house_matrix[i][cost2] else (cost2,cost1)
            for j in range(2,K):
                if paint_house_matrix[i][j]<paint_house_matrix[i][cost1]:
                    cost2=cost1
                    cost1=j
                elif paint_house_matrix[i][j]<paint_house_matrix[i][cost2]:
                    cost2=j    
        print("The paint house matrix for debugging purposes:",paint_house_matrix)                
        return min(paint_house_matrix[-1])
    
if __name__=="__main__":

        N=int(input("Enter the N: "))
        K=int(input("Enter the number if colors: "))

        min_cost=find_Min_Cost(N,K)
        print("The Minimum Cost: ",min_cost)


