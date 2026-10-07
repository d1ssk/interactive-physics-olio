(() => {
  const locale = new URLSearchParams(location.search).get('lang') === 'ja' ? 'ja' : 'en';
  const view = window.inflationView;
  const strings = {
    en: {
      backgroundTitle:'From an oscillating mode to a frozen field', backgroundIntro:'Exact de Sitter test scalar. Compare the gradient and background terms, then switch to the mode functions. Time increases to the right.',
      squeezingTitle:'Squeezing grows while its direction settles', squeezingIntro:'The same canonical quadratures as the main animation, extended to four e-folds after Hubble crossing.',
      basisTitle:'One Gaussian state, two choices of modes', basisIntro:'First count the real field degrees of freedom; then change the oscillator basis. The matrices below describe the full same state, without discarding a mode.',
      samplesTitle:'From vacuum fluctuations to a correlated random amplitude', samplesIntro:'The same 256 Gaussian samples are transported by the exact Hamiltonian flow. Move the slider to compare the initial and evolved clouds on identical, fixed axes.',
      acousticTitle:'Random amplitudes, different temporal phases', acousticIntro:'Eight sample histories in each ensemble, and the mean squared amplitude of 4096 realizations. Play the cursor or move it by hand to compare the samples at the same acoustic time.',
      display:'Display',frequency:'Gradient versus background',mode:'Mode functions', magnitude:'Squeezing magnitude',angle:'Broad-axis angle',
      frequencyNote:'The background term overtakes the gradient at \\(x=\\sqrt2\\), before Hubble crossing at \\(x=1\\). The evolution is smooth; the sign change of the effective squared frequency is not a new causal horizon.',
      modeNote:'Solid: the physical field mode divided by its late-time amplitude. Dashed: the rescaled field mode. Real and imaginary parts depend on the chosen positive-frequency phase; the magnitude does not. The physical field freezes while the rescaled variable grows.',
      squeezingNote:'Vertical dotted line: Hubble crossing. The dashed asymptote is \\(r\\simeq N\\). The angle approaches zero, measured from the positive \\(Q\\) axis. Its early-time value has little geometric significance because the ellipse is nearly circular.',
      halfspace:'One member of each nonzero pair lies in the shaded half-space. The opposite amplitude is fixed by the reality condition; the selected complex amplitude has two independent real components.',
      fieldNotOperator:'This is a reality condition on field amplitudes, not an identification of the two annihilation operators.',
      sameState:'Traveling pair ⇄ cosine and sine modes: the same Gaussian state',traveling:'Traveling-wave basis',standing:'Standing-wave basis',paired:'paired',independent:'independent',
      travelingNote:'Pair coherence links opposite traveling modes.',standingNote:'The cosine and sine amplitudes undergo identical single-mode squeezing.',
      epoch:'Epoch \\(x=k/(aH)\\)',early:'Inside · 12',cross:'Crossing · 1',late:'Outside · 0.2',travelingCov:'Traveling-mode covariance',standingCov:'Standing-mode covariance',
      matrixNote:'Blue: positive covariance; orange: negative; uncolored: zero. Both matrices use one fixed color scale. The standing matrix has two identical blocks with no cross-mode correlations. The traveling matrix has correlations between opposite modes. Matrix entries are dimensionless; each vacuum variance is 1/2.',
      sampleTime:'E-fold time of the evolved cloud',initialCloud:'Initial · \\(x=12\\)',evolvedCloud:'Evolved state',
      sampleNote:'Axes are \\(Q\\) and \\(P\\), with identical units and fixed limits. The black outline is the same unit-Mahalanobis Wigner contour as in the main animation, not a boundary for all samples. The dashed orange line is the conditional mean of \\(P\\) given \\(Q\\). The markers sample a positive Wigner density; they are not simultaneous sharp measurements or quantum-particle trajectories.',
      play:'Play',pause:'Pause',reset:'Reset',acousticTime:'Acoustic time (a moving cursor on the fixed histories)',coherent:'Coherent: random amplitudes, common zeros',incoherent:'Incoherent: independent temporal quadratures',
      acousticNote:'Upper axes: acoustic time \\(u\\) and normalized real amplitude. Lower axes: the same \\(u\\) and mean squared amplitude. Each ensemble has unit total initial variance in expectation. Thin lines show finite-sample power; thick lines show the exact ensemble prediction. Spatial Fourier phases remain random. This undriven oscillator omits baryons, gravity, neutrinos, damping, recombination, and sky projection.',
      plotAlt:'Interactive scientific plot; pan to move and use the wheel to zoom. The caption defines its axes.',halfAlt:'A schematic Fourier plane with the positive half-space shaded and a pair of opposite wavevectors',
      error:'This figure could not load. Reload the page to try again.',
    },
    ja: {
      backgroundTitle:'振動するモードから凍結する場へ',backgroundIntro:'厳密de Sitter時空のテストスカラー場です。勾配項と背景項を比較し、モード関数の表示に切り替えてみてください。時間は右向きに進みます。',
      squeezingTitle:'スクイージングの増大と方向の収束',squeezingIntro:'主アニメーションと同じ正準quadratureを使い、Hubble crossing後4 e-foldまで表示します。',
      basisTitle:'同じGaussian状態を二つの基底で見る',basisIntro:'まず実場の自由度を数え、次に振動子の基底を変えます。下の行列はモードを捨てずに、同じ状態全体を記述しています。',
      samplesTitle:'真空のゆらぎから相関したランダム振幅へ',samplesIntro:'同じ256個のGaussianサンプルを、厳密なHamilton流で運びます。スライダーを動かし、共通の固定軸で初期分布と発展後の分布を比較してください。',
      acousticTitle:'ランダムな振幅と時間位相の違い',acousticIntro:'各集団から8本の実現例を示し、4096個の実現値から振幅の二乗平均を求めています。カーソルを再生するか手で動かし、同じ音響時刻で比較してください。',
      display:'表示',frequency:'勾配項と背景項',mode:'モード関数',magnitude:'スクイージングの大きさ',angle:'長軸の角度',
      frequencyNote:'背景項が勾配項を上回るのは\\(x=\\sqrt2\\)であり、\\(x=1\\)のHubble crossingより前です。時間発展は滑らかです。有効振動数の二乗の符号変化は、新しい因果的地平線を意味しません。',
      modeNote:'実線：物理的な場のモードを晩期の振幅で規格化したもの。破線：再スケールした場のモード。実部・虚部は選んだ正周波数の位相規約に依存しますが、絶対値は依存しません。元の場は凍結し、再スケールした変数は成長します。',
      squeezingNote:'縦の点線はHubble crossing、破線は漸近式\\(r\\simeq N\\)です。角度は正の\\(Q\\)軸から測り、ゼロに近づきます。初期には楕円がほぼ円なので、角度の値の幾何学的な意味は弱くなります。',
      halfspace:'各非零波数対の片方を、色付きの半空間から選びます。反対側の振幅は実条件で決まり、選んだ一つの複素振幅に二つの独立な実成分が含まれます。',
      fieldNotOperator:'これは場の振幅の実条件であり、二つの消滅演算子を同一視する式ではありません。',
      sameState:'進行波の対 ⇄ cos・sinの定在波：同じGaussian状態',traveling:'進行波基底',standing:'定在波基底',paired:'対の相関',independent:'独立',
      travelingNote:'逆向きの進行波モード間に対の相関があります。',standingNote:'cos成分とsin成分は同一の単一モード・スクイージングを受けます。',
      epoch:'時期 \\(x=k/(aH)\\)',early:'内側 · 12',cross:'crossing · 1',late:'外側 · 0.2',travelingCov:'進行波モードの共分散',standingCov:'定在波モードの共分散',
      matrixNote:'青は正の共分散、オレンジは負、無色はゼロです。両行列で固定の色スケールを共有します。定在波の行列は同じ二つのブロックに分かれ、モード間の相関はゼロです。進行波の行列には逆向きのモード間の相関があります。成分は無次元量で、真空の各分散は2分の1です。',
      sampleTime:'発展後の分布のe-fold時刻',initialCloud:'初期分布 · \\(x=12\\)',evolvedCloud:'時間発展した分布',
      sampleNote:'座標は\\(Q\\)、\\(P\\)で、単位の長さと軸範囲は共通・固定です。黒い輪郭は主アニメーションと同じMahalanobis距離1のWigner等高線であり、全サンプルを囲む境界ではありません。オレンジの破線は\\(Q\\)を与えたときの\\(P\\)の条件付き平均です。点は正のWigner密度のサンプルであり、同時に鋭く測定した値や量子粒子の軌道ではありません。',
      play:'再生',pause:'一時停止',reset:'最初に戻る',acousticTime:'音響時刻（固定した各実現例の上をカーソルが動きます）',coherent:'コヒーレント：振幅はランダム、零点は共通',incoherent:'非コヒーレント：時間方向の二成分が独立',
      acousticNote:'上段の軸は音響時刻\\(u\\)と規格化した実振幅、下段は同じ\\(u\\)と振幅の二乗平均です。両集団の初期分散の総和は期待値で1です。細線は有限個のサンプル平均、太線は厳密な集団平均を表します。空間Fourier位相はランダムなままです。外力のない振動子の模型であり、バリオン、重力、ニュートリノ、減衰、再結合、天球への射影は含みません。',
      plotAlt:'インタラクティブな科学図。ドラッグで移動、ホイールで拡大できます。軸の定義は説明文に記載しています。',halfAlt:'片側の半空間を色付けし、反対向きの波数の対を示したFourier平面の模式図',
      error:'図を読み込めませんでした。ページを再読み込みしてください。',
    },
  };
  const t=strings[locale], $=id=>document.getElementById(id);
  document.documentElement.lang=locale; document.title=t[`${view}Title`];
  $('figure-title').textContent=t[`${view}Title`]; $('figure-intro').textContent=t[`${view}Intro`];
  document.querySelectorAll('[data-i18n]').forEach(el=>el.textContent=t[el.dataset.i18n]);
  document.querySelectorAll('.chart').forEach(el=>el.setAttribute('aria-label',t.plotAlt));
  $('k-plane').setAttribute('aria-label',t.halfAlt);
  let data;
  const blue='#397da9',gold='#a37d2b',orange='#d26541',green='#569d88',ink='#28333d';
  const palette=[blue,orange,green,gold,'#8768a6','#469da6','#bc678c','#707780'];
  const config={responsive:true,displaylogo:false,scrollZoom:true,modeBarButtonsToRemove:['lasso2d','select2d']};
  const plots=[];
  function layout(xTitle,yTitle,extra={}) {
    return {margin:{l:52,r:15,t:28,b:56},font:{family:'system-ui, sans-serif',size:11,color:ink},
      paper_bgcolor:'rgba(0,0,0,0)',plot_bgcolor:'rgba(0,0,0,0)',dragmode:'pan',
      xaxis:{title:{text:xTitle,standoff:8},gridcolor:'#ded6cc',zeroline:false},
      yaxis:{title:{text:yTitle,standoff:6},gridcolor:'#ded6cc',zeroline:false},
      legend:{orientation:'h',y:1.16,x:0,font:{size:10}},uirevision:view,...extra};
  }
  function line(x,y,name,color,dash='solid',width=2) {return {type:'scatter',mode:'lines',x,y,name,line:{color,dash,width},hovertemplate:'%{x:.3f}, %{y:.4g}<extra>%{fullData.name}</extra>'};}
  function vertical(x,color=ink,dash='dot') {return {type:'line',xref:'x',yref:'paper',x0:x,x1:x,y0:0,y1:1,line:{color,dash,width:1}};}
  async function plot(id,traces,spec) {
    await Plotly.react($(id),traces,spec,config); if(!plots.includes(id)) plots.push(id);
    window.dispatchEvent(new Event('physics-atlas:plot-rendered'));
  }
  let mathQueue=Promise.resolve();
  function typeset(targets) {
    mathQueue=mathQueue.then(async()=>{
      if(!window.MathJax?.startup?.promise) await new Promise(resolve=>window.addEventListener('physics-atlas:mathjax-ready',resolve,{once:true}));
      await MathJax.startup.promise; MathJax.typesetClear(targets); await MathJax.typesetPromise(targets);
      window.dispatchEvent(new Event('physics-atlas:mathjax-ready'));
    });
    return mathQueue;
  }
  async function background() {
    const e=data.evolution, isMode=$('background-choice').value==='mode';
    MathJax.typesetClear([$('background-equation'),$('background-note')]);
    let traces,spec;
    if(isMode) {
      traces=[];
      ['Real','Imaginary','Magnitude'].forEach((name,i)=>{
        traces.push(line(e.n,e.field[i],`${name}: field`,[blue,orange,green][i]));
        traces.push(line(e.n,e.rescaled[i],`${name}: rescaled`,[blue,orange,green][i],'dash',1.5));
      });
      spec=layout('E-folds from Hubble crossing','Normalized mode amplitude',{shapes:[vertical(0)],legend:{orientation:'h',y:1.02,yanchor:'bottom',font:{size:10}},margin:{l:52,r:15,t:window.innerWidth<650?150:80,b:55}});
      $('background-equation').textContent='\\(F_q=\\sqrt{2k}f_k\\), \\(F_\\phi=\\sqrt{2k^3}f_k/(aH)=xF_q\\)';
    } else {
      traces=[line(e.n,e.reference,'Gradient term',blue),line(e.n,e.background,'Background term',orange)];
      spec=layout('E-folds from Hubble crossing','Term divided by squared wavenumber',{
        yaxis:{type:'log',title:{text:'Term divided by squared wavenumber'},gridcolor:'#ded6cc'},shapes:[vertical(0),vertical(e.equalTerms,orange,'dash')],
        annotations:[{x:0,y:1,xref:'x',yref:'paper',text:'Hubble crossing',showarrow:false,xanchor:'left',yanchor:'bottom',font:{size:10}},{x:e.equalTerms,y:0,xref:'x',yref:'paper',text:'Equal terms',showarrow:false,xanchor:'right',yanchor:'bottom',font:{size:10,color:orange}}],
      });
      $('background-equation').textContent='\\(k^2/k^2=1\\), \\((a^{\\prime\\prime}/a)/k^2=2/x^2\\), \\(\\omega_k^2/k^2=1-2/x^2\\)';
    }
    $('background-note').textContent=isMode?t.modeNote:t.frequencyNote;
    await plot('background-plot',traces,spec); await typeset([$('background-equation'),$('background-note')]);
  }
  async function squeezing() {
    const e=data.evolution;
    await plot('magnitude-plot',[line(e.n,e.r,'Exact',blue),line(e.n,e.asymptote.map((r,i)=>e.n[i]<0?null:r),'Late-time asymptote',orange,'dash')],layout('E-folds from crossing','Squeezing magnitude',{shapes:[vertical(0)]}));
    await plot('angle-plot',[line(e.n,e.angle,'Broad-axis angle',orange)],layout('E-folds from crossing','Angle in degrees',{showlegend:false,shapes:[vertical(0)]}));
  }
  async function basis() {
    const frame=data.basis[Number($('basis-time').value)];
    for(const name of ['traveling','standing']) {
      const labels=name==='traveling'?['Q_+','P_+','Q_-','P_-']:['Q_R','P_R','Q_I','P_I'];
      const target=$(`${name}-matrix`); if(window.MathJax?.typesetClear) MathJax.typesetClear([target]); target.replaceChildren();
      const table=document.createElement('table');table.className='covariance';table.setAttribute('aria-label',t[`${name}Cov`]);
      const head=document.createElement('tr'); const empty=document.createElement('th');head.append(empty);
      labels.forEach(label=>{const cell=document.createElement('th');cell.scope='col';cell.textContent=`\\(${label}\\)`;head.append(cell);}); table.append(head);
      frame[name].forEach((row,i)=>{
        const tr=document.createElement('tr'),th=document.createElement('th');th.scope='row';th.textContent=`\\(${labels[i]}\\)`;tr.append(th);
        row.forEach(value=>{const td=document.createElement('td');td.textContent=Math.abs(value)<1e-7?'0':value.toFixed(2);
          const alpha=Math.min(Math.abs(value)/13,.75);td.style.backgroundColor=value>0?`rgba(57,125,169,${alpha})`:`rgba(210,101,65,${alpha})`;tr.append(td);});table.append(tr);
      });target.append(table);
    }
    await typeset([$('traveling-matrix'),$('standing-matrix')]);
  }
  function cloudTraces(frame) {
    return [
      {type:'scatter',mode:'markers',x:frame.points[0],y:frame.points[1],name:'Wigner samples',marker:{size:4,color:blue,opacity:.5},hoverinfo:'skip'},
      line(frame.ring[0],frame.ring[1],'Wigner contour',ink),
      line([-12,12],frame.relation,'Conditional mean',orange,'dash',1.5),
    ];
  }
  function cloudLayout() {
    const result=layout('Field quadrature','Momentum quadrature',{showlegend:false,margin:{l:40,r:12,t:15,b:45}});
    result.xaxis.range=[-12,12];result.yaxis.range=[-12,12];result.yaxis.scaleanchor='x';result.yaxis.scaleratio=1;
    return result;
  }
  async function samples(initial=false) {
    const f=data.samples[Number($('sample-time').value)];
    $('sample-x').value=f.x.toFixed(3);$('sample-n').value=f.n.toFixed(3);
    $('sample-time').setAttribute('aria-valuetext',`N = ${f.n.toFixed(3)}, x = ${f.x.toFixed(3)}`);
    if(initial) await plot('initial-cloud',cloudTraces(data.samples[0]),cloudLayout());
    await plot('evolved-cloud',cloudTraces(f),cloudLayout());
  }
  let acousticPlaying=false, acousticHandle=null, acousticIndex=0;
  function acousticStop(){acousticPlaying=false;clearTimeout(acousticHandle);$('acoustic-play').textContent=t.play;}
  async function cursor() {
    const u=data.acoustic.u[acousticIndex];$('acoustic-u').value=u.toFixed(2);$('acoustic-time').value=acousticIndex;
    $('acoustic-time').setAttribute('aria-valuetext',`u = ${u.toFixed(2)}`);
    await Promise.all(['coherent-plot','incoherent-plot','power-plot'].map(id=>Plotly.relayout($(id),{shapes:[vertical(u,ink,'solid')]})));
  }
  async function acousticStep(){if(!acousticPlaying)return; acousticIndex=Math.min(acousticIndex+1,data.acoustic.u.length-1);await cursor();if(acousticIndex===data.acoustic.u.length-1){acousticStop();return;}if(acousticPlaying)acousticHandle=setTimeout(acousticStep,60);}
  async function acoustic() {
    const a=data.acoustic;
    for(const type of ['coherent','incoherent']) {
      await plot(`${type}-plot`,a[type].curves.map((values,i)=>line(a.u,values,`Realization ${i+1}`,palette[i],'solid',1.4)),layout('Acoustic time','Normalized real amplitude',{showlegend:false,shapes:[vertical(0)],yaxis:{range:[-3,3],title:{text:'Normalized real amplitude'},gridcolor:'#ded6cc'}}));
    }
    await plot('power-plot',[
      line(a.u,a.coherent.power,'Coherent: sample',blue,'dot',1),line(a.u,a.incoherent.power,'Incoherent: sample',gold,'dot',1),
      line(a.u,a.coherent.exact,'Coherent: exact',blue,'solid',3),line(a.u,a.incoherent.exact,'Incoherent: exact',gold,'dash',3),
    ],layout('Acoustic time','Normalized mean square',{shapes:[vertical(0)],margin:{l:52,r:15,t:window.innerWidth<650?110:65,b:55},legend:{orientation:'h',y:1.02,yanchor:'bottom',font:{size:10}}}));
    ['acoustic-play','acoustic-reset','acoustic-time'].forEach(id=>$(id).disabled=false);
  }
  // Only the background equations and covariance tables change mathematical text.
  $('background-choice').addEventListener('change',()=>background().catch(fail));
  $('basis-time').addEventListener('change',()=>basis().catch(fail));
  let sampleBusy=false,samplePending=false;
  $('sample-time').addEventListener('input',async()=>{samplePending=true;if(sampleBusy)return;sampleBusy=true;try{while(samplePending){samplePending=false;await samples();}}catch(e){fail(e);}finally{sampleBusy=false;}});
  $('acoustic-time').addEventListener('input',()=>{acousticStop();acousticIndex=Number($('acoustic-time').value);cursor().catch(fail);});
  $('acoustic-play').addEventListener('click',()=>{if(acousticPlaying)return acousticStop();if(acousticIndex===data.acoustic.u.length-1)acousticIndex=0;acousticPlaying=true;$('acoustic-play').textContent=t.pause;acousticStep().catch(fail);});
  $('acoustic-reset').addEventListener('click',()=>{acousticStop();acousticIndex=0;cursor().catch(fail);});
  document.addEventListener('visibilitychange',()=>{if(document.hidden)acousticStop();});window.addEventListener('pagehide',acousticStop);
  let resizeTimer;
  window.addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(async()=>{
    if(!data)return;
    await Promise.all(plots.map(id=>Plotly.Plots.resize($(id))));
    if(view==='background')await background();
    if(view==='acoustic')await Plotly.relayout($('power-plot'),{'margin.t':window.innerWidth<650?110:65});
  },100);});
  function fail(){acousticStop();$('support-error').hidden=false;$('support-error').textContent=t.error;}
  Promise.all([window.plotReady,fetch('supporting.json').then(r=>{if(!r.ok)throw Error('data');return r.json();})]).then(async([,payload])=>{
    data=payload;
    await typeset([document.querySelector(`section[data-view="${view}"]`)]);
    if(view==='background')await background();if(view==='squeezing')await squeezing();if(view==='basis')await basis();
    if(view==='samples'){await samples(true);$('sample-time').disabled=false;}if(view==='acoustic')await acoustic();
    document.documentElement.dataset.ready='true';
    window.dispatchEvent(new Event('physics-atlas:plot-rendered'));
  }).catch(fail);
})();
