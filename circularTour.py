class Solution:
    def tour(self, lis, n):
        start = 0
        balance = 0
        total_deficit = 0

        for i in range(n):
            # Calculer la balance actuelle d'essence
            balance += lis[i][0] - lis[i][1]

            # Si la balance est négative, le point de départ actuel n'est pas viable
            if balance < 0:
                # Mettre à jour le point de départ au prochain index
                start = i + 1
                # Ajouter le déficit courant au total_deficit
                total_deficit += balance
                # Réinitialiser la balance à zéro pour recommencer à partir du nouveau point de départ
                balance = 0

        # Vérifier si le tour est possible avec le point de départ trouvé
        if balance + total_deficit >= 0:
            return start
        else:
            return -1

# Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = []
        for i in range(n):
            petrol = arr[2 * i]
            distance = arr[2 * i + 1]
            lis.append([petrol, distance])
        print(Solution().tour(lis, n))
