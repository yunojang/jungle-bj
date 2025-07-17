from function_visualizer import FunctionVisualizer

visualizer = FunctionVisualizer()


n, s = list(map(int, input().split()))
nums = list(map(int, input().split()))

cnt = [0]


@visualizer.visualize(param_names=["sum", "depth"])
def combi(sum=0, depth=0, is_in=False):
    if depth == n:
        if sum == s and is_in:
            cnt[0] += 1
        return

    combi(sum, depth + 1, is_in or False)
    combi(sum + nums[depth], depth + 1, True)


combi()
print(cnt[0])
visualizer.render("combi", "png")
