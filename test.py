# Input data
x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [2, 3, 5, 5, 7, 8, 10, 13]

# Hyperparameters
learning_rate = 0.02
steps = 5

# Initial weights and bias
w = 0
b = 0

# Training loop
for step in range(steps):
    # Forward pass
    y_pred = [w * xi + b for xi in x]
    
    # Compute mean squared error loss
    mse_loss = sum((y_pred[i] - y[i]) ** 2 for i in range(len(x))) / len(x)
    
    # Compute gradients
    dw = (2/len(x)) * sum(x[i] * (y_pred[i] - y[i]) for i in range(len(x)))
    db = (2/len(x)) * sum(y_pred[i] - y[i] for i in range(len(x)))
    
    # Update weights and bias
    w -= learning_rate * dw
    b -= learning_rate * db
    
    # Print progress
    print(f"Step {step + 1}: Weight = {w:.3f}, Bias = {b:.3f}, Loss = {mse_loss:.3f}")













# x = [0, 1, 2, 3, 4, 5, 6, 7]
# y = [2, 3, 5, 5, 7, 8, 10, 13]

# n = 8

# ste = 5

# p = 0.02

# w = 0
# b = 0

# for _ in range(ste):
#     grad_w = 0
#     grad_b = 0
#     for i in range(len(x)):
#         grad_w += (y[i] - w*x[i] - b) * x[i]
#         grad_b += (y[i] - w*x[i] - b)

#     grad_w = grad_w * (-2/n)
#     grad_b = grad_b * (-2/n)

#     w = w - (p * grad_w)
#     b = b - (p * grad_b)

#     w = round(w, 3)
#     b = round(b, 3)

#     print("w:", w)
#     print("b:", b)









import math 
 
def weight_gradient(y, yhat, x): 
    return round((y - yhat) * x, 3) 
 
def bias_gradient(y, yhat): 
    return round((y - yhat), 3) 
 
def y_hat(x, w, b): 
    return round(1 / (1 + math.e ** (-1 * (w * x + b))), 3) 
 
x = list(map(int, input().split())) 
y = list(map(int, input().split())) 
 
w, b = 0, 0 
w_res, b_res = [], [] 
 
for iteration in range(1, 6): 
    w_total, b_total = 0, 0 
     
    for i in range(len(x)): 
        yhat = y_hat(x[i], w, b) 
        w_total += weight_gradient(y[i], yhat, x[i]) 
        b_total += bias_gradient(y[i], yhat) 
         
    w_grad = round(-1 * w_total / len(x), 3) 
    b_grad = round(-1 * b_total / len(x), 3) 
     
    w = round(w - 0.02 * w_grad, 3) 
    b = round(b - 0.02 * b_grad, 3) 
     
    w_res.append(w) 
    b_res.append(b) 
     
print("w: ", end = ' ') 
for i in range(5): 
    print(w_res[i], end=' ') 
print() 
 
print("b: ", end = ' ') 
for i in range(5): 
    print(b_res[i], end=' ') 
print()































































# Function to round numbers to three decimal places
def round_to_three_decimal_places(num):
    # Round to three decimal places
    rounded_num = round(num, 3)
    # Check if there are more than 3 decimal places and the fourth decimal is 5 or greater
    if len(str(rounded_num).split('.')[1]) > 3 and int(str(rounded_num).split('.')[1][3]) >= 5:
        # If yes, round up to four decimal places
        return round(num, 4)
    else:
        # If not, round to three decimal places
        return rounded_num

# Input data
x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [2, 3, 5, 5, 7, 8, 10, 13]

# Hyperparameters
learning_rate = 0.02
steps = 5

# Initial weights and bias
w = 0
b = 0

# Training loop
for step in range(steps):
    # Forward pass
    y_pred = [w * xi + b for xi in x]
    
    # Compute mean squared error loss
    mse_loss = sum((y_pred[i] - y[i]) ** 2 for i in range(len(x))) / len(x)
    
    # Compute gradients
    dw = (2/len(x)) * sum(x[i] * (y_pred[i] - y[i]) for i in range(len(x)))
    db = (2/len(x)) * sum(y_pred[i] - y[i] for i in range(len(x)))
    
    # Update weights and bias
    w -= learning_rate * dw
    b -= learning_rate * db
    
    # Print progress
    print(f"Step {step + 1}: Weight = {round_to_three_decimal_places(w)}, Bias = {round_to_three_decimal_places(b)}, Loss = {round_to_three_decimal_places(mse_loss)}")


























# w:  0.018 0.034 0.049 0.062 0.074 
# b:  0.0 -0.0 -0.001 -0.002 -0.003 



