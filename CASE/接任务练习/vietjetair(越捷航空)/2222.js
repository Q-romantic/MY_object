

function rsa(pub, data) {
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(pub);
    var out = encrypt.encrypt(data);
    return out
}

message = '{"adultCount":1,"arrival":"HAN","childCount":0,"currency":"USD","daysAfterDeparture":0,"daysBeforeDeparture":0,"departureDate":"2023-03-31","departurePlace":"SGN","infantCount":0,"oneway":1,"requestId":"QX3DFYOI1XCV-1679758370760","sessionId":null,"user-agent-ls-data":"7a5766db-24b1-4fa4-a342-db1c2bb740ef-1679758370759","x-power-web-s-d":"6130551311-1911511106-43cb-af10-1e42ca8b66e7","_signature":"bab214cf948b348015144acedfa604cb744aa896e1bb05dcc460f7353ee837db"}'
public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAok58IrYXjeFjb6hPgrcvKis43ARDVIqowS2AJKivDp4+8uKDCWnjzBZTsuVvwKPzvVCxBzON2/DPpHU3wnRtdKSVzWju7HMKhuLxe04FsVw8+xvZTmguBj4jTczNLSLjK13lQr46J8j7JrmVUlPqGxIL/Bd3HNAIFuarZQkDsgx5fvdNrMbmT4edr1b3A8wRkhfo9tuE5Tmlx0YVUwybzcI6hgLggCfNwwaClXyBt08NbGSIBcKYKjiQErND0EOnWcGyto7EhkpgGRfAeESo3hbmsiabThLd4t9iOWVHFSl+7B0q+1IGFjSo9qkvNdMUI4ZYdIKq+nCHufpuFMl7SwIDAQAB"

out = rsa(public_key, message)
console.log(out)