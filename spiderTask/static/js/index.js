window.onload = function () {
    var box = document.getElementById("box");
    var audioVice = document.getElementById("vice");
    audioVice.volume = 0.4;
    //歌曲标识
    count = 1;
    //歌曲总数
    var allMusicNum = 7;

    //播放和暂停
    var playBut = document.getElementById("play");
    var pauseBut = document.getElementById("pause");
    playBut.addEventListener("click", function () {
        audioVice.play();
        playBut.style.display = 'none';
        pauseBut.style.display = "block";
    }, false);
    pauseBut.addEventListener("click", function () {
        audioVice.pause();
        pauseBut.style.display = "none";
        playBut.style.display = "block";
    }, false);


    // 上一首下一首调用播放函数
    function playSong(songId, songName, tag) {
        // var songId = obj.target.getAttribute('songId'); //曲Id
        // var songName = obj.target.textContent; //曲名
        // var tag = obj.target.getAttribute('tag'); // 歌曲分类

        console.log(songId, songName, tag);

        var $userSpan = $('div#user span');
        var userName = ''; // 用户名
        if ($userSpan.length != 0) {
            userName = $userSpan.text();
        }

        //请求网易云音乐接口
        $.get(
            "https://api.imjad.cn/cloudmusic/", {
                'type': 'song',
                'id': songId,
                'br': '128000'
            }, function (data, state) {
                //这里显示从服务器返回的数据
                console.log(data);
                console.log(data.data[0].url);
                var songUrl = data.data[0].url;
                audioVice.src = songUrl;
                audioVice.play();
                pauseBut.style.display = "block";
                playBut.style.display = "none";

                $('#songname').text('正在播放：' + songName);

            }
        );

        // 请求自己后台，记录用户听过歌曲
        $.get(
            "/spidertask/myrec", {
                songId: songId,
                songName: songName,
                songTag: tag,
                userName: userName,
            }, function (data, state) {
                //这里显示从服务器返回的数据
                console.log(data);
            }
        );
    }


    //上一曲下一曲
    var beforeBut = document.getElementById("before");
    var afterBut = document.getElementById("after");
    beforeBut.addEventListener("click", function () {
        var $currentRed = $('#red');
        if ($currentRed.length != 0) {
            // 找到上一个标红播放
            var $prevSong = $currentRed.prev();
            if ($prevSong.length != 0) {
                //有上一首情况
                var songId = $prevSong.attr('songId');
                var tag = $prevSong.attr('tag');
                var songName = $prevSong.text();
                $prevSong.css("color", "red");
                $prevSong.attr('id', 'red');
                playSong(songId, songName, tag);
            } else {
                // 没有上一首情况，从尾部开始播放
                var leftSongList = document.getElementById('songList');
                var $lastnode = $(leftSongList.lastChild);
                var songId = $lastnode.attr('songId');
                var tag = $lastnode.attr('tag');
                var songName = $lastnode.text();
                $lastnode.css("color", "red");
                $lastnode.attr('id', 'red');
                playSong(songId, songName, tag);
            }
            // 将上一首恢复原来状态
            $currentRed.attr('id', '');
            $currentRed.css('color', '#74bd59');

        } else {
            //从头开始播放
            var leftSongList = document.getElementById('songList');
            var $firstnode = $(leftSongList.firstChild);
            var songId = $firstnode.attr('songId');
            var tag = $firstnode.attr('tag');
            var songName = $firstnode.text();
            $firstnode.css("color", "red");
            $firstnode.attr('id', 'red');
            playSong(songId, songName, tag);
        }

    }, false);

    afterBut.addEventListener("click", next, false);

    function next() {
        var $currentRed = $('#red');
        if ($currentRed.length != 0) {
            // 找到上一个标红播放
            var $nextSong = $currentRed.next();
            if ($nextSong.length != 0) {
                //有下一首情况
                var songId = $nextSong.attr('songId');
                var tag = $nextSong.attr('tag');
                var songName = $nextSong.text();
                $nextSong.css("color", "red");
                $nextSong.attr('id', 'red');
                playSong(songId, songName, tag);
            } else {
                // 没有下一首情况，从头部开始播放
                var leftSongList = document.getElementById('songList');
                var $firstChild = $(leftSongList.firstChild);
                var songId = $firstChild.attr('songId');
                var tag = $firstChild.attr('tag');
                var songName = $firstChild.text();
                $firstChild.css("color", "red");
                $firstChild.attr('id', 'red');
                playSong(songId, songName, tag);
            }
            // 将上一首恢复原来状态
            $currentRed.attr('id', '');
            $currentRed.css('color', '#74bd59');

        } else {
            //从头开始播放
            var leftSongList = document.getElementById('songList');
            var $firstnode = $(leftSongList.firstChild);
            var songId = $firstnode.attr('songId');
            var tag = $firstnode.attr('tag');
            var songName = $firstnode.text();
            $firstnode.css("color", "red");
            $firstnode.attr('id', 'red');
            playSong(songId, songName, tag);
        }


    }

    //播放模式的实现
    var loopObj = document.getElementById("loop");
    var orderObj = document.getElementById("order");
    //循环模式
    loopObj.addEventListener("click", function () {
        loopObj.style.display = "none";
        orderObj.style.display = "block";
        audioVice.loop = "";
        timer = setInterval(isEnd, 1000);
    }, false);

    //顺序模式
    orderObj.addEventListener("click", function () {
        orderObj.style.display = "none";
        loopObj.style.display = "block";
        audioVice.loop = "loop";
        clearInterval(timer);
    }, false);


    //检测是否歌唱完毕
    var timer = setInterval(isEnd, 1000);

    function isEnd() {
        if (audioVice.currentTime == audioVice.duration) {
            next();
        }
    }

    //实现音量的调节
    var vLenghtObj = document.getElementById("vLength");
    var vLength1Obj = document.getElementById("vLengh1");
    var vcObj = document.getElementById("vC");
    var min = vcObj.offsetLeft;
    var max = vcObj.offsetLeft + 200;
    vcObj.addEventListener("mousedown", function (e) {
        var baseX = e.pageX;
        box.addEventListener("mouseover", mover, false);

        function mover(e) {
            //计算偏移量
            var moveX = 0;
            moveX = e.pageX - baseX;
            baseX = e.pageX;
            local = vcObj.offsetLeft + moveX;
            //桌面样式的改变
            if (local > max) {
                //小球超出设置
                vcObj.style.left = max + "px";
            } else if (local < min) {
                vcObj.style.left = min + "px";
            }
            vcObj.style.left = local + "px";
            vLength1Obj.style.width = moveX + parseInt(window.getComputedStyle(vLength1Obj, null).width) + "px";

            //音量值的设定
            volumeNum = moveX / 200;
            audioVice.volume = audioVice.volume + volumeNum;
            // console.log(audioVice.volume);

        }

        vcObj.addEventListener("mouseup", function () {
            box.removeEventListener("mouseover", mover, false);
        }, false);
        box.addEventListener("mouseup", function () {
            box.removeEventListener("mouseover", mover, false);
        }, false);
    }, false);

    //静音
    var volumeBut = document.getElementById("volume");
    var muteBut = document.getElementById("mute");
    volumeBut.addEventListener("click", function () {
        volumeBut.style.display = "none";
        muteBut.style.display = "block";
        audioVice.volume = 0;
        vcObj.style.left = "710px";
        vLength1Obj.style.width = "0px";
    }, false);

    //取消静音
    muteBut.addEventListener("click", function () {
        volumeBut.style.display = "block";
        muteBut.style.display = "none";
        audioVice.volume = 0.4;
        vcObj.style.left = "790px";
        vLength1Obj.style.width = "80px";
    }, false);

    //	实现播放进度
    var dLengthObj = document.getElementById("dLength");
    var dLength1Obj = document.getElementById("dLength1");
    var dcObj = document.getElementById("dC");
    var planTimer = setInterval(function () {
        var movePiex = audioVice.currentTime / audioVice.duration * 600;
        dLength1Obj.style.width = movePiex + "px";
//		dcObj.style.left = (window.getComputedStyle(dcObj,null).left)
        dcObj.style.left = 300 + movePiex + "px";

    }, 10);

    //设置播放时间
    var currentObj = document.getElementById("currentTime");
    var endObj = document.getElementById("endTime");
    var currentTime = setInterval(function () {
        var endtime = audioVice.duration;
        var currenttime = audioVice.currentTime;
        currenttime = calculateTime(currenttime);
        endtime = calculateTime(endtime);
        currentObj.innerHTML = currenttime;
        endObj.innerHTML = endtime;
    }, 100);

    //计算时间函数封装
    function calculateTime(second) {
        var tt = (parseFloat(second / 60).toFixed(2)).toString();
        var tInt = tt.split(".")[0];
        var tFloat = parseInt(parseFloat("0." + tt.split(".")[1]) * 60);
        var timeStr = tInt + ":" + tFloat;
        // console.log(timeStr);
        return timeStr;

    }


    var playlist = [
        ['2507067464', '华语'],
        ['2193563343', '经典'],
        ['2500857826', '伤感'],
        ['2836875765', '摇滚'],
        ['3226995486', '流行'],
    ];

    function getSongByListTag() {
        var index = Math.floor((Math.random() * playlist.length));
        var cplayTag = playlist[index][1];
        var playId = playlist[index][0];
        $.get("https://api.imjad.cn/cloudmusic/", {
            type: 'playlist',
            id: playId
        }, function (result) {
            var songList = result.playlist.tracks;
            var playlistTag = cplayTag;
            // console.log(songList);
            var $ul = $("#songList");
            // var tag = $("<li id='tag' data='" + playlistTag + "' style='margin-bottom: 10px;'>类别：" + playlistTag + "</li>");
            // $ul.append(tag);
            for (var i = 0; i < songList.length; i++) {
                var $li = $("<li tag='" + playlistTag + "' class='persong' songId='" + songList[i].id + "'>" + songList[i].name.substring(0, 30) + "</li>");
                // var $li = $("<div class=\"alert alert-success\" songId='" + songList[i].id + "' onclick='getSong(this)'>" + songList[i].name.substring(0, 30) + "</div>");
                $ul.append($li);
            }
        });


    }

    getSongByListTag(); // 初始化歌单列表

    // 为换一批按钮添加事件
    var change = document.getElementById("change");
    change.addEventListener("click", function () {
        var $ul = $("#songList");
        $ul.empty();
        getSongByListTag();
    }, false);

    function getSong(obj) {
        var songId = obj.target.getAttribute('songId'); //曲Id
        var songName = obj.target.textContent; //曲名
        var tag = obj.target.getAttribute('tag'); // 歌曲分类

        var $userSpan = $('div#user span');
        var userName = ''; // 用户名
        if ($userSpan.length != 0) {
            userName = $userSpan.text();
        }

        // 将左侧列表中的样式转化成最初的样子
        var $currentRed = $('#red');
        $currentRed.attr('id', '');
        $currentRed.css('color', '#74bd59');

        //请求网易云音乐接口
        $.get(
            "https://api.imjad.cn/cloudmusic/", {
                'type': 'song',
                'id': songId,
                'br': '128000'
            }, function (data, state) {
                //这里显示从服务器返回的数据
                console.log(data);
                console.log(data.data[0].url);
                var songUrl = data.data[0].url;
                audioVice.src = songUrl;
                audioVice.play();
                pauseBut.style.display = "block";
                playBut.style.display = "none";

                $('#songname').text('正在播放：' + songName);

            }
        );

        // 请求自己后台，记录用户听过歌曲
        $.get(
            "/spidertask/myrec", {
                songId: songId,
                songName: songName,
                songTag: tag,
                userName: userName,
            }, function (data, state) {
                //这里显示从服务器返回的数据
                console.log(data);
            }
        );
    }

    $(document).on("click", ".persong", function (e) {
        getSong(e);
    });


    // 为搜索按钮添加点击事件
    var serachBtn = document.getElementById("search_button");
    serachBtn.addEventListener('click', function () {
        var searchContent = $('#appendedInputButton')[0].value;
        $('input#appendedInputButton').val('');
        $.get(
            "https://api.imjad.cn/cloudmusic/", {
                type: 'search',
                search_type: 1,
                s: searchContent,
            }, function (data, state) {
                //这里显示从服务器返回的数据
                console.log(data);
                var songs = data.result.songs;
                // var $ul = $("#sameList");
                var $ul = $("#queryRet");
                $ul.empty();
                for (var i = 0; i < 15; i++) {
                    var $li = $("<li tag='搜索' class='persong' songId='" + songs[i].id + "'>" + songs[i].name.substring(0, 13) + "</li>");
                    $ul.append($li);
                }


            }
        );
    });


    // 推介冒泡向上特效
    var tkTimer = setInterval(function () {
        var box = document.getElementById('box');
        var recsong = document.createElement("div");
        recsong.setAttribute('class', 'alert alert-success persong');
        recsong.setAttribute('id', 'rec');

        // 异步请求
        var userId = '';

        var $userSpan = $('div#user span');
        var userName = ''; // 用户名
        if ($userSpan.length != 0) {
            userName = $userSpan.text();
        }

        $.get(
            "/spidertask/getRec", {
                userName: userName,
            }, function (data, state) {
                songInfo = data.data;
                recsong.textContent = songInfo[1] + '-' + songInfo[2];
                recsong.setAttribute('songId', songInfo[0]);
                recsong.setAttribute('tag', '推介');
                box.appendChild(recsong);
                //歌曲上移定时器
                var songMoveTimer = setInterval(function () {
                    recsong.style.top = recsong.offsetTop - 5 + "px";
                    if (recsong.offsetTop <= 100) {
                        box.removeChild(recsong);
                        clearInterval(songMoveTimer);
                    }
                }, 100);
                recsong.time = songMoveTimer;

            }
        );

    }, 4000);


}