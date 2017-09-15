function main() {
    if (window.navigator.userAgent.indexOf("Edge") > -1) {
        $('body').css('zoom', '110%');
        $('.my-slide div li').css('font-size', '1.8rem');
        
    } else if (window.navigator.userAgent.indexOf("OPR") > -1 || window.navigator.userAgent.indexOf("Opera") > -1) {
        $('body').css('zoom', '100%');
    }
    $('body').fadeIn(500);

    $('.buttons, .block').mouseenter(function(){
        $(this).fadeTo('fast', .7);
    });
    $('.buttons, .block').mouseleave(function(){
        $(this).fadeTo('fast', 1);
    });

    $('.review').mouseenter(function(){
        $(this).toggleClass('my-active');
    });
    $('.review').mouseleave(function(){
        $(this).toggleClass('my-active');
    });

    $('input[type="submit"]').mouseenter(function(){
        $(this).fadeTo('slow', .7);
    });
    $('input[type="submit"]').mouseleave(function(){
        $(this).fadeTo('slow', 1);
    });

    var firefox = navigator.userAgent.search(/Firefox/) > -1;
    if (firefox)
        $('.logos').css('height', '220px');
    $('input[type="text"], textarea, input[type="submit"]').focus(function(){
        if (firefox)
            $(this).css('outline-style', 'solid');
        $(this).css('outline-color', '#F5F5F5');    
    });

    var handleMatchMedia2 = function (mediaQuery) {
            if (mediaQuery.matches) {
                $('.camon p').css('font-size', '3rem');
            } else {
                $('.camon p').css('font-size', '4rem');
            }
        },
        mql2 = window.matchMedia('all and (max-width: 1000px)');
    handleMatchMedia2(mql2);
    mql2.addListener(handleMatchMedia2);



    /* hint */

    (function($){
    $(function() {

        $('span.jQtooltip').each(function() {
            var el = $(this);
            var title = el.attr('title');
            if (title && title != '') {
                el.attr('title', '').append('<p>' + '<i class="fa fa-map-marker" aria-hidden="true"></i>' + '   ' + title + '</p>');
                var width = el.find('p').width();
                var height = el.find('p').height();
                el.hover(
                    function() {
                        el.find('p')
                            .clearQueue()
                            .delay(200)
                            .animate({width: width + 20, height: height + 20}, 200).show(200)
                            .animate({width: width, height: height}, 200);
                    },
                    function() {
                        el.find('p')
                            .animate({width: width + 20, height: height + 20}, 150)
                            .animate({width: 'hide', height: 'hide'}, 150);
                    }
                ).mouseleave(function() {
                    if (el.children().is(':hidden')) el.find('p').clearQueue();
                });
            }
        })
    })
    })(jQuery)

    /* button UP */

    $(function() {
    
    $(window).scroll(function() {
    
    if($(this).scrollTop() > 500) {
    
    $('.toTop').fadeIn();
    
    } else {
    
    $('.toTop').fadeOut();
    
    }
    
    });
    
    $('.toTop').click(function() {
    
    $('body,html').animate({scrollTop:0},500);
    
    });
    
    });
}
$(document).ready(main);