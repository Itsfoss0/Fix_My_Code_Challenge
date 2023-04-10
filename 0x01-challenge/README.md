![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

![Hot-fix](../code.jpeg)

## Fix my code challenge 1
Debugging issues in the implementation of some projects. 

Lets jump right in. 

### Task 0 - Server status
I just started a new Flask project and the first thing I’m putting in place is a route for the status of my API (super important for a load balancer implementation).

But I don’t know why it’s not working…

Could you look at it and fix it please?
```
$ python -m api.v1.app 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
```
$ curl -XGET http://0.0.0.0:5000/api/v1/status
{
  "error": "Not found"
}
$
```