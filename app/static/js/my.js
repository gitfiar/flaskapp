  $( function(){

      var $grid = $('#grid').masonry({
        // init with no items
        itemSelector: 'NONE',
        percentPosition: true,
        columnWidth: '.grid-sizer',
        gutter: '.gutter-sizer'
      });

      // reset itemSelector to load grid-item
      $grid.masonry( 'option', {
        itemSelector: '.grid-item',
      })
      
      $grid.masonryImagesReveal( $('#grid').find('.grid-item') );

    });

    $.fn.masonryImagesReveal = function( $items ) {
      var msnry = this.data('masonry');
      var itemSelector = msnry.options.itemSelector;
      // hide by default
      $items.hide();
      // append to container
      this.append( $items );
      $items.imagesLoaded().progress( function( imgLoad, image ) {
        // get item
        // image is imagesLoaded class, not <img>, <img> is image.img
        var $item = $( image.img ).parents( itemSelector );
        // un-hide item
       $item.show();
        // masonry does its thing
        msnry.appended( $item );
      });
      
      return this;
    };
$(document).ready(function() {  
    $("img.lazy-load").lazyload({ 
        　　    effect : "slideDown", //渐现，show(直接显示),fadeIn(淡入),slideDown(下拉)
        　　　　threshold : -100, //预加载，在图片距离屏幕180px时提前载入
        　　　　event: 'scroll',  // 事件触发时才加载，click(点击),mouseover(鼠标划过),sporty(运动的),默认为scroll（滑动）
        　　　　//container: $("#container"), // 指定对某容器中的图片实现效果
        　　　　failure_limit:2 //加载2张可见区域外的图片,lazyload默认在找到第一张不在可见区域里的图片时则不再继续加载,但当HTML容器混乱的时候可能出现可见区域内图片并没加载出来的情况
        　　}); 
    const sliderImages = document.querySelectorAll('.grid__img');

    function checkSlide(e) {
       sliderImages.forEach(sliderimage => {
            // 滑动到图片显示的一半
            const slideAt = window.innerHeight + window.scrollY - sliderimage.height / 2;
            // 图片底部距文档顶部的距离
            const imageBottom = sliderimage.offsetTop + sliderimage.height;
            // 图片是否已经显示了一半
            const isHalfShown = slideAt > sliderimage.offsetTop;
            // 图片是否已经被完全滚动出去
            const isNotScrolledPast = window.scrollY < imageBottom;
            if (isHalfShown && isNotScrolledPast) {
                sliderimage.classList.add('active');
            } else {
                sliderimage.classList.remove('active');
            }
        });
    }
    // 监听滚动
    window.addEventListener('scroll', checkSlide);

});
Echo.init({
    offset:0,
    throttle: 3000

})
