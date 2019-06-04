const renderProduct = ({id, title, image}) => (
  `
    <li class="product">
      <img class="product__image" src="${ image }">
      <span class="product__name">
          ${ title }
      </span>
      <a class="product__link" href="/products/${ id }">
      </a>
  </li>
  `
);
