---
title: "¡Llegó Polymer v3!"
description: "Los GDG de Andalucía se reunieron en Málaga... ¡Y nosotros teníamos que estar allí!"
date: "2017-08-28"
categories:
    - "post"
tags:
    - "GDG"
    - "Comunidad"
    - "Crónica"
#cardthumbimage: "/images/default.jpg" #optional: solid color if unset
cardheaderimage: "/images/default.jpg" #optional: solid color if unset
cardbackground: "#B71C1C" #optional: card background color; only shows when no image specified
cardtitlecolor: "#fff" #optional: can be changed to make text visible over card image
"author":
    name: "Israel Blancas"
    description: "Google Developer Group Granada Lead Organizer"
    website: "http://iblancasa.com/"
    twitter: "https://twitter.com/iblancasa"
    github: "https://github.com/iblancasa"
    image: "/images/israel.png"
---
<style>
  twitterwidget {margin: 0 auto;}
</style>

<iframe width="560" height="450" src="https://www.youtube.com/embed/4X4tCIJeo8w" frameborder="0" allowfullscreen></iframe>

La semana pasada se celebró el [Polymer Summit](https://summit.polymer-project.org/)
2017 en Copenhague. Entre otras cosas, [se ha presentado la versión preview
de Polymer 3 (que está disponible en su repositorio de GitHub, en la rama 3.0-preview)](https://github.com/Polymer/polymer/tree/3.0-preview).
Se han presentado muchas novedades y voy a intentar resumir aquí las que, al
menos para mí, son más importantes.

Para los que no conozcáis Polymer (mal hecho), os comento que es una biblioteca
para crear tus propias etiquetas HTML, las cuales pueden tener una vista y/o
un comportamiento. Esto se encuentra dentro de la “programación modular”
(que ha tomado mucha fuerza en los últimos años en el front-end) y nos
permite desarrollar aplicaciones mantenibles, con una mayor facilidad de
testeo y de una forma más rápida. A esto se suma la posibilidad de aprovechar
mejor las capacidades del navegador (pudiendo acceder de forma más sencilla a
  las APIs nativas, por ejemplo). ¿Cual es la gracia frente a frameworks como
  Angular? Con Polymer buscamos crear WebComponents, que puedan ser reutilizados
  después desde esos frameworks.

WebComponents es un estándar (aunque aún se está trabajando en ello). Se basa
en las siguientes tecnologías:

* Templates: la vista del elemento (otros componentes y etiquetas HTML).
* Shadow DOM: el DOM del componente es local al objeto, de forma que hay encapsulación.
* Custom Elements: elementos HTML personalizados, es decir, la posibilidad de
crear tus propias etiquetas.
* HTML Imports: posibilidad de importar otros componentes.

<blockquote class="twitter-tweet" data-lang="es" style="margin: 0 auto;"><p lang="en" dir="ltr">Tune in now! The <a href="https://twitter.com/hashtag/PolymerSummit?src=hash">#PolymerSummit</a> keynote is streaming live from <a href="https://twitter.com/hashtag/Copenhagen?src=hash">#Copenhagen</a> 🇩🇰 with <a href="https://twitter.com/wmginsberg">@wmginsberg</a> &amp; <a href="https://twitter.com/FredKSchott">@FredKSchott</a>.<a href="https://t.co/h3JflPyIIZ">https://t.co/h3JflPyIIZ</a> <a href="https://t.co/qFS9Y88cVI">pic.twitter.com/qFS9Y88cVI</a></p>&mdash; Polymer (@polymer) <a href="https://twitter.com/polymer/status/899904167816433664">22 de agosto de 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Mientras la mayor parte de estas funcionalidades ya se encuentran incorporadas
en los principales navegadores web, otras tantas no (aunque poco a poco, los
desarrolladores de los frameworks de front-end y navegadores se están
poniendo de acuerdo).

<blockquote class="twitter-tweet" data-lang="es"><p lang="en" dir="ltr">ES Modules will be native in Chrome next Sept. 5 🙀 <a href="https://twitter.com/hashtag/PolymerSummit?src=hash">#PolymerSummit</a> <a href="https://t.co/kQX23ZIZ0y">pic.twitter.com/kQX23ZIZ0y</a></p>&mdash; Carlos Azaustre (@carlosazaustre) <a href="https://twitter.com/carlosazaustre/status/899912318070530049">22 de agosto de 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

De este Polymer Summit ha destacado la eliminación de los HTMLImports en
Polymer. Hace tiempo que se sabía que iban a ser descartados y ya ha llegado el
momento. En Polymer 3, pasamos de los HTMLImports a los ES Modules, como ya
venían haciendo otros frameworks. Y Chrome implementará, de forma nativa, la
posibilidad de utilizar ES Modules a partir de su versión de septiembre
(mientras los demás navegadores trabajan en ello).

Otra noticia, también esperada, era la utilización de NPM o yarn en lugar de
bower. La utilización de cualquiera de estas herramientas es otro paso más
hacia la utilización de una misma herramienta para la gestión de las distintas
bibliotecas Javascript.

<blockquote class="twitter-tweet" data-lang="es"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/PolymerSummit?src=hash">#PolymerSummit</a> scenery 🖼 <a href="https://t.co/Xf5f0hvILN">pic.twitter.com/Xf5f0hvILN</a></p>&mdash; Matthew McNulty (@mattsmcnulty) <a href="https://twitter.com/mattsmcnulty/status/901387356095344640">26 de agosto de 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Y, aunque todo esto rompa con las versiones anteriores, es otro esfuerzo
para conseguir un estándar y acabar con la problemática del front-end: aparece
un nuevo framework (serio) cada 3 meses y la interoperabilidad no es posible.

<iframe width="560" height="450" src="https://www.youtube.com/embed/JH6jEcLxJEI" frameborder="0" allowfullscreen></iframe>
