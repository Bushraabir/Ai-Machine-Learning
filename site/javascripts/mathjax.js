/* Place this at: docs/javascripts/mathjax.js */
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    packages: { '[+]': ['boldsymbol'] },
    macros: {
      /* Commonly used ML notation */
      RR: "\\mathbb{R}",
      EE: "\\mathbb{E}",
      PP: "\\mathbb{P}",
      NN: "\\mathbb{N}",
      XX: "\\mathcal{X}",
      YY: "\\mathcal{Y}",
      HH: "\\mathcal{H}",
      LL: "\\mathcal{L}",
      DD: "\\mathcal{D}",
      ww: "\\mathbf{w}",
      xx: "\\mathbf{x}",
      yy: "\\mathbf{y}",
      bb: "\\mathbf{b}",
      mmu: "\\boldsymbol{\\mu}",
      SSigma: "\\boldsymbol{\\Sigma}",
      ttheta: "\\boldsymbol{\\theta}",
      norm: ["\\left\\| #1 \\right\\|", 1],
      abs:  ["\\left| #1 \\right|", 1],
      argmin: "\\operatorname*{arg\\,min}",
      argmax: "\\operatorname*{arg\\,max}",
    }
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});