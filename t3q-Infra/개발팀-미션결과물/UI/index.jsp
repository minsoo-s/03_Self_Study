<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
    <head>
        <title>커피 점수 예측</title>
        <meta charset="utf-8" />
    </head>

    <body>
    <h2>커피 점수 예측</h2>
    <h3>커피 정보를 입력해주세요.</h3>
    <hr />
    <form id="inputform">
        <table>
        <tr>
            <td>Aroma(향미)</td>
            <td><input type="text" id="aroma" name="aroma" /></td>
            <td>점</td>
        </tr>
        <tr>
            <td>Flavor(맛)</td>
            <td><input type="text" id="flavor" name="flavor" /></td>
            <td>점</td>
        </tr>
        <tr>
            <td>Acidity(산도)</td>
            <td><input type="text" id="acidity" name="acidity" /></td>
            <td>점</td>
        </tr>
        <tr>
            <td>Balance(발란스)</td>
            <td><input type="text" id="balance" name="balance" /></td>
            <td>점</td>
        </tr>
        </table>
        <input type="button" value="점수 예측하기" onclick="predict()" />
        <input type="reset" value="다시 입력하기" />
        <input type="button" value="테이블 보기" onclick="databases()" />
    </form>
    <span id = "text"></span>
    </body>

<script>
    var xhr;
    function databases() {
        xhr = new XMLHttpRequest();
        xhr.onreadystatechange = show_table;
        xhr.open("GET", "http://172.16.16.132:30800/data");
        xhr.send(null);
    }
    function show_table() {
        if(xhr.readyState == 4 && xhr.status == 200){
            var form = document.createElement("form");
            var table = JSON.stringify(JSON.parse(xhr.response));
            console.log(table);

            form.action = "db.jsp";
            form.method = "post";

            var input = document.createElement("input");
            input.setAttribute("type", "hidden");
            input.setAttribute("name", "table");
            input.setAttribute("value", table);
            form.appendChild(input);
            document.body.appendChild(form);
            form.submit();
        } else if (xhr.readyState < 4) {
            document.getElementById("text").innerHTML
                = "응답 대기 중";
        }
    }

    function predict() {
        xhr = new XMLHttpRequest();
        xhr.onreadystatechange = show_pred;
        xhr.open("POST", "http://172.16.16.132:30800/datasend");
        var req = {
            'aroma':document.getElementById("aroma").value,
            'flavor':document.getElementById("flavor").value,
            'acidity':document.getElementById("acidity").value,
            'balance':document.getElementById("balance").value
        };
        console.log(req);
        xhr.setRequestHeader("Content-Type", 'application/json; charset=UTF-8');
        xhr.send(JSON.stringify(req));
    }
    function show_pred() {
        if(xhr.readyState == 4 && xhr.status == 200){
            var score = JSON.parse(xhr.response);
            var url = 'ex.jsp?param='+score.score;
            location.href = url;
        } else if (xhr.readyState < 4) {
            document.getElementById("text").innerHTML
                = "응답 대기 중";
        }
    }
</script>
</html>
