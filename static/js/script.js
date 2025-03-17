//https://cdnjs.cloudflare.com/ajax/libs/Glide.js/3.0.2/glide.js

var glideHeroPeek = new Glide(".heropeek", {
  type: "carousel",
  animationDuration: 1000,
  autoplay: 4000,
  focusAt: "1",
  startAt: 1,
  perView: 1,
  // set a value to show the previous and next slides peeking in
  peek: {
    before: 70,
    after: 70,
  },
  gap: 20,
//   gap: 0,
});

glideHeroPeek.mount();
