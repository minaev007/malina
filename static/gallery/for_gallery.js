        function main() {
            $(document).keydown(function(key) {
                switch(parseInt(key.which,10)) {
                    // Left arrow key pressed
                    case 37:
                        $('.dg-prev').click();
                        break;
                    // Right Arrow Pressed
                    case 39:
                        $('.dg-next').click();
                        break;
                }
            });
            $('.gallery-photo').swipe( {
                    swipeLeft:leftSwipe2,
                    swipeRight:rightSwipe2,
                    threshold:0
            });
            function leftSwipe2(event){
                $('.dg-next').click();
            }
            function rightSwipe2(event){
                $('.dg-prev').click();
            }    
        }
        $(document).ready(main);