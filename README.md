# test-server

## 필요사항
* Python 3.8

## 실행방법
### 의존성 설지
```
$ pip install -r requirements.txt
```
### 서버 실행
```
$ python -m flask --app main run
```
## API 사용법
### API 주소
`http://127.0.0.1:5000/<연>/<월>/<일>` 로 접근시 JSON 양식으로 작성된 해당 일자의 판매 데이터를 받을 수 있다.

## API 응답 양식
```
application/json:
  schema:
    type: array
    items:
      type: object
      properties:
        InvoiceNo:
          type: string
        StockCode:
          type: string
        Description:
          type: string
        Quantity:
          type: integer
        InvoiceDate:
          type: string
        UnitPrice:
          type: number
        CustomerID:
          type: number
        Country:
          type: number
```