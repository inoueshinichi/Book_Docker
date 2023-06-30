
// デバッグテーブルの更新
var refreshTable = function () {
    $.ajax({
        type: 'get',
        url: '/api/v1/keys/',
        success: function (j) {
            $('#table').empty()
            var hline = '<tr><th scope="col">#</th><th scope="col">Key</th>'
            hline += '<th scope="col">Value</th></tr>'
            $('#table').append(hline)

            var index = 1
            for (var key in j) {
                var line = '<tr><th scope="row">' + index + '</th>'
                line += '<td>' + key + '</td><td>' + j[key] + '</td></tr>'
                $('#table').append(line)
                index++
            }
        }
    })
}

$(function () {
    // Get
    $('#get-button').click(
        function () {
            $.ajax({
                type: 'get',
                url: '/api/v1/keys/' + $('#key').val(),
                success: function (j, status, xhr) {
                    $('#response-body').text(JSON.stringify(j, null, '  '))
                    $('#response-code').text(xhr.status)
                },
                error: function (d) {
                    $('#response-body').text(d.responseText)
                    $('#response-code').text(d.status)
                }
            })
        }
    )

    // Post
    $('#post-button').click(
        function () {
            $.ajax({
                type: 'post',
                url: '/api/v1/keys/' + $('#key').val(),
                data: $('#value').val(),
                success: function (j, status, xhr) {
                    $('#response-body').text(JSON.stringify(j, null, '  '))
                    $('#response-code').text(xhr.status)
                    refreshTable()
                },
                error: function (d) {
                    $('#response-body').text(d.responseText)
                    $('#response-code').text(d.status)
                }
            })
        }
    )

    // Put
    $('#put-button').click(
        function () {
            $.ajax({
                type: 'put',
                url: '/api/v1/keys/' + $('#key').val(),
                data: $('#value').val(),
                success: function (j, status, xhr) {
                    $('#response-body').text(JSON.stringify(j, null, '  '))
                    $('#response-code').text(xhr.status)
                    refreshTable()
                },
                error: function (d) {
                    $('#response-body').text(d.responseText)
                    $('#response-code').text(d.status)
                }
            })
        }
    )

    // Delete
    $('#delete-button').click(
        function () {
            $.ajax({
                type: 'delete',
                url: '/api/v1/keys/' + $('#key').val(),
                success: function (j, status, xhr) {
                    $('#response-body').text(JSON.stringify(j, null, '  '))
                    $('#response-code').text(xhr.status)
                    refreshTable()
                },
                error: function (d) {
                    $('#response-body').text(d.responseText)
                    $('#response-code').text(d.status)
                }
            })
        }
    )

    // Key入力に対するイベントハンドラ
    $('#key').keyup(function () {
        var newText = '/api/v1/keys/' + $('#key').val()
        $('#request-url').text(newText)
        $('#response-body').text('')
        $('#response-code').text('')
    })

    // Value入力に対するイベントハンドラ
    $('#value').keyup(function () {
        $('#request-body').text($('#value').val())
        $('#response-body').text('')
        $('#response-code').text('')
    })

    refreshTable()
    setInterval(refreshTable, 5000) // 5s
})

