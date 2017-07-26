function main() {
    checking = false;

    /* slider */

    var slideWidth=995;
    var sliderTimer;

    var sliderChildLength = $('.my-slidewrapper').children().length;

    $(function(){

        $('.my-slidewrapper').width(sliderChildLength*slideWidth);
        sliderTimer=setInterval(debNext,3000);
        $('.my-viewport').hover(function(){
            clearInterval(sliderTimer);
        },function(){
            sliderTimer=setInterval(debNext,3000);
        }
    );

        $(window).keyup(function(key) {
            window.checking = true;
            switch(parseInt(key.which,10)) {
            // Left arrow key pressed
            case 37:
                clearInterval(sliderTimer);
                sliderTimer=setInterval(debNext,3000);
                debPast();
                break;
            // Right Arrow Pressed
            case 39:
                clearInterval(sliderTimer);
                sliderTimer=setInterval(debNext,3000);
                debNext();
                break;
        }
    });
    
    $(".my-viewport").swipe( {
            swipeLeft:leftSwipe,
            swipeRight:rightSwipe,
            threshold:0
    });
    function leftSwipe(event){
        window.checking = true;
        clearInterval(sliderTimer);
        debNext();
        sliderTimer=setInterval(debNext,3000);
    }
    function rightSwipe(event){
        window.checking = true;
        clearInterval(sliderTimer);
        debPast();
        sliderTimer=setInterval(debNext,3000);
    }

});
    var debNext = _.debounce(function nextSlide(){
        var currentSlide=parseInt($('.my-slidewrapper').data('current'));
        currentSlide++;
        if (currentSlide>=sliderChildLength)
        {
            currentSlide=0;   
        }
        if (checking) {
        $('.my-slidewrapper').animate({left: -currentSlide*slideWidth},300).data('current',currentSlide);
        } else {
        $('.my-slidewrapper').animate({left: -currentSlide*slideWidth},800).data('current',currentSlide);
        }
        window.checking = false;
    }, 300);

    var debPast = _.debounce(function pastSlide(){
        var currentSlide=parseInt($('.my-slidewrapper').data('current'));
        currentSlide--;
        if(currentSlide<0)
        {
            currentSlide=3;   
        }
        if (checking) {
        $('.my-slidewrapper').animate({left: -currentSlide*slideWidth},300).data('current',currentSlide);
        } else {
        $('.my-slidewrapper').animate({left: -currentSlide*slideWidth},800).data('current',currentSlide);            
        }
        window.checking = false;
    }, 300);

    if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
        $('#fullpage').css('min-width', '1000px');
    } else {
        if (window.screen.width > 1500) {
            $("#fullpage").fullpage({
                anchors:['main','contacts'],
                scrollBar:false,
                scrollOverflow:true,
                slidesNavigation:true,
                navigationPosition:'left',
                slidesNavPosition:'top',
                loopTop:true,
                loopBottom:true,
                loopHorizontal:false
                            
            });
        }

        var handleMatchMedia = function (mediaQuery) {
                if (mediaQuery.matches) {
                    slideWidth=736;
                    $('.buttons').removeClass('animate-to-big');
                    $('.buttons').addClass('animate-to-small');
                    $('.navigation a').addClass('media-navigation');
                    $('.my-viewport').removeClass('my-slide-big');
                    $('.my-viewport').addClass('my-slide-small');
                    $('.my-slide').removeClass('my-slide-big');
                    $('.my-slide').addClass('my-slide-small');
                    $('.my-slide img').removeClass('my-slide-img-big');                    
                    $('.my-slide img').addClass('my-slide-img-small');                    
                } else {
                    slideWidth=995;
                    $('.buttons').removeClass('animate-to-small');
                    $('.buttons').addClass('animate-to-big');
                    $('.navigation a').removeClass('media-navigation');
                    $('.my-viewport').removeClass('my-slide-small');
                    $('.my-viewport').addClass('my-slide-big');
                    $('.my-slide').removeClass('my-slide-small');
                    $('.my-slide').addClass('my-slide-big');
                    $('.my-slide img').removeClass('my-slide-img-small');                    
                    $('.my-slide img').addClass('my-slide-img-big');                                    
                }
                console.log(slideWidth);
            },
            mql = window.matchMedia('all and (max-width: 1020px)');
        handleMatchMedia(mql);
        mql.addListener(handleMatchMedia);
    }
};
$(document).ready(main);