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

