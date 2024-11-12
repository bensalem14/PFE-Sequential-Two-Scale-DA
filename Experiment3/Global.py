seed_value = 41
eps=1/50
h=10
step=0.001
mu,sigma=0,0.1
macrostep=30
microstep=1
model_name = "ToyModel6"
x_0 = [1]
w=60

info = """
seed_value = {0}
eps={1}
h={2}
step={3}
mu,sigma={4},{5}
macrostep={6}
microstep={7}
model_name = {8}
x_0 = {9}
w={10}""".format(seed_value,eps,h,step,mu,sigma,macrostep,microstep,model_name,x_0,w)
print(info)