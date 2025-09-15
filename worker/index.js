const keys = require('./keys');
const redis = require('redis');

const redisClient = redis.createClient({
  host: keys.redisHost,
  port: keys.redisPort,
  retry_strategy: () => 1000
});
const sub = redisClient.duplicate();

function fib(index) {
  const fibSequence = [1, 1];
  for (let i = 2; i <= index; i++) {
    fibSequence[i] = fibSequence[i - 1] + fibSequence[i - 2];
  }
  return fibSequence[index];
}

sub.on('message', (channel, message) => {
  redisClient.hset('values', message, fib(parseInt(message)));
});
sub.subscribe('insert');
