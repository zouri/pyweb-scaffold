/**
 * Created by lp on 2016/8/2.
 */
/**  导航搜索...*/
$(function(){
    function check(e) {//������ɰ��س�

        var bt = document.getElementById("ss_nr");
        var e = window.event || arguments.callee.caller.arguments[0];

        if (e && e.keyCode == 13 ) {

            alert(bt.value);

        }
    }


    function test() {//������ɰ��Ŵ�
        var txtValue = document.getElementById("ss_nr").value;
        alert(txtValue);
    }

    //左导航
    sp_h()
    window.onresize=function(){
        sp_h()
    }
    function sp_h(){
        //alert(1)
        var winh=$(window).height();
        var navlefth=winh-298-69;
        /*if($('#main').height()<navlefth){
            $('#navleft').height(navlefth)
        }else{
            $('#navleft').height($('#main').height())
        }*/
        /*alert($('#main').height())
        $('#navleft').height($('#main').height())
        if($('#navleft').height()<navlefth){
            $('#navleft').height(navlefth)
        }*/
    }

    //导航
    var pphd,aboutus,xhcp,shgy;
    $('#aboutus').bind('mouseenter',function(){
        $('.navli').hide();
        $('#about').show();
    })
    $('#aboutus').bind('mouseleave',function(){
        aboutus=setTimeout(function(){
            $('#about').hide();
        },250)
    })

    $('#pphd').bind('mouseenter',function(){
        $('.navli').hide();
        $('#band').show();
    })
    $('#pphd').bind('mouseleave',function(){
        pphd=setTimeout(function(){
            $('#band').hide();
        },250)
    })

    $('#xhcp').bind('mouseenter',function(){
        $('.navli').hide();
        $('#pronav').show();
    })
    $('#xhcp').bind('mouseleave',function(){
        xhcp=setTimeout(function(){
            $('#pronav').hide();
        },250)
    })

    $('#shgy').bind('mouseenter',function(){
        $('.navli').hide();
        $('#shehui').show();
    })
    $('#shgy').bind('mouseleave',function(){
        shgy=setTimeout(function(){
            $('#shehui').hide();
        },250)
    })

    $('.navli').bind('mouseenter',function(){
         //alert(1)
        clearTimeout(aboutus);
        clearTimeout(pphd);
        clearTimeout(xhcp);
        clearTimeout(shgy);
    })


    $('.navli').bind('mouseleave',function(){
       $('.navli').hide();
    })


    $('#aboutus,#gsjs').click(function(){
        window.location.href=siteUrl+'about/recommend';
        //window.open('about.html')
    })
    $('#gsls').click(function(){
        window.location.href=siteUrl+'about/history';
        //window.open('History.html')
    })
    $('#gsry').click(function(){
        window.location.href=siteUrl+'about/honor';
        //window.open('Honor.html')
    })
    $('#gszx').click(function(){
        window.location.href=siteUrl+'news/list&page=1';
        //window.open('newlist.html')
    })

    $('#pphd,#jchd').click(function(){
        window.location.href=siteUrl+'activity/act';
        //window.open('band.html')
    })
    $('#ggsp').click(function(){
        window.location.href=siteUrl+'activity/adv&page=1';
        //window.open('ad.html')
    })

    $('#xhcp,#pro1').click(function(){
        window.location.href=siteUrl+'product/list';
        //window.open('pro1.html')
    })
    $('#pro2').click(function(){
        window.location.href=siteUrl+'product/list';
        //window.open('pro2.html')
    })
    $('#pro3').click(function(){
        window.location.href=siteUrl+'product/list';
        //window.open('pro3.html')
    })
    $('#pro4').click(function(){
        window.location.href=siteUrl+'product/list';
        //window.open('pro4.html')
    })
    $('#pro5').click(function(){
        window.location.href=siteUrl+'product/list';
        //window.open('pro5.html')
    })
    $('#pro6').click(function(){
        window.location.href=siteUrl+'product/list';
        //window.open('pro6.html')
    })
    $('#pro7').click(function(){
        window.location.href=siteUrl+'product/list';
        //window.open('pro7.html')
    })
    $('#pro8').click(function(){
        window.location.href=siteUrl+'product/list';
        //window.open('pro8.html')
    })

    $('#shgy,#gj').click(function(){
        window.location.href=siteUrl+'benefit/book';
        //window.open('soc.html')
    })
    $('#zr').click(function(){
        window.location.href=siteUrl+'benefit/report';
        //window.open('soc2.html')
    })

    $('#rcsc').click(function(){
        window.location.href=siteUrl+'job/list';
        //window.open('Recruitment.html')
    })
    $('#hrwq').click(function(){
        window.location.href='http://www.crc.com.cn/other/group/';
        //window.open('http://www.crc.com.cn/other/group/')
    })

})

