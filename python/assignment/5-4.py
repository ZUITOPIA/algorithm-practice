# 1912943 고주희
# 이진트리를 위한 노드 클래스
class TNode:
    def __init__ (self, data, left, right):	# 생성자
        self.data = data 			# 노드의 데이터
        self.left = left			# 왼쪽 자식을 위한 링크
        self.right = right			# 오른쪽 자식을 위한 링크


# 1번을 해보세요! - 전위 순회
def preorder(n) :
    if n is not None:
        print(n.data, end=" ")
        preorder(n.left)
        preorder(n.right)


# 2번을 해보세요!
n = int(input())
binary_tree = [TNode(0,0,0) for _ in range(n)]

for i in range(n):
    data, left, right = [int(m) for m in input().split()[:3]]

    binary_tree[i].data = data
    binary_tree[i].left = binary_tree[left-1] if left > 0 else None
    binary_tree[i].right = binary_tree[right-1] if right > 0 else None


# 출력합니다!
root = binary_tree[0]
print('Pre-Order : ', end='')
preorder(root)
print()