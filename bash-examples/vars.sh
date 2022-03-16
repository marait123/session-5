# Environment variables are managed by your shell. 
# The difference between environment variables and regular shell variables (6.8) is that 
# a shell variable is local to a particular instance of the shell (such as a shell script), 
# while environment variables are "inherited" by any program you start, 
# including another shell (38.4). That is, the new process gets its own copy of these variables,
#  which it can read, modify, and pass on in turn to its own children. 
# In fact, every UNIX process (not just the shell) passes its environment variables to its child processes.

export AWS_PROFILE=mohammed

echo "environment var: " $AWS_PROFILE

AWS_PROFILE1=mohammed1

echo "normal var: " $AWS_PROFILE1

x=1
y=2
z=`expr $x + $y`
echo $x "+" $y "=" $z
