# Introduction
1. What is .eds?


## Electronic Data Sheet
Tệp .eds (Electronic Data Sheet) được sử dụng để mô tả cấu trúc và thông tin về các đối tượng CANopen trong một thiết bị. Dưới đây là một ví dụ đơn giản về nội dung tệp node_definition.eds để đại diện cho một node CANopen đơn giản có một đối tượng SDO (Service Data Object).
```xml

```
Trong ví dụ này:
* Tệp .eds bắt đầu với một phần tử <eds> để đánh dấu tệp.
* Trong <e>, bạn có thể định nghĩa các thuộc tính cho node CANopen của bạn.
* Mỗi thuộc tính được định nghĩa bằng một phần tử <p>. Các thuộc tính này bao gồm index (số thứ tự duy nhất của thuộc tính), name (tên của thuộc tính), dataType (kiểu dữ liệu của thuộc tính), accessType (quyền truy cập), và objectType (kiểu đối tượng).
* <pdes> chứa mô tả ngắn gọn của thuộc tính.

Trong ví dụ này, chúng ta chỉ định ba thuộc tính đơn giản cho một node CANopen. Trong thực tế, tệp .eds có thể chứa nhiều thông tin khác nhau về đối tượng CANopen, bao gồm mô tả của các đối tượng PDO (Process Data Object) và nhiều thông tin khác.

Lưu ý rằng cấu trúc cụ thể của tệp .eds có thể khác nhau tùy thuộc vào thiết bị cụ thể và đối tượng CANopen bạn đang làm việc. Để tạo một tệp .eds phù hợp với thiết bị của bạn, bạn cần tuân theo tài liệu của nhà sản xuất hoặc chuẩn CANopen.