'''
Created on Jun 29, 2015

@author: navid
'''
from pythonreveal.api import *






def get_frontpage(p):
    page = p.frontpage()
    page.title('Pruning weighted complex networks')
    author = page.author('Navid Dianati')
    author.institution('The LazerLab, Northeastern University')
    author.institution('IQSS Harvard University')


def get_section_intro(p):
    '''
    1- Networks are cool! Example: FEC occupations colored
    2- Two possible problems: 
        - Network is too dense.
        - Network has too much noise.
    3- Examples: 
        - correlation matrix in biology
        - similarity matrix between data points (dimensionality reduction)
    4- Examples:
        - Co-occurrence network
        - Pairwise event count network
    5- Major distinction: 
        - Sparsification: aprroximation
        - Pruning: separation of noise from signal
    '''
    p.pagesection('Simplifying Complex Networks')

    
    page = p.page('No one likes hairball graphs')
    page.im('massachusetts-ocupations-attorney-hairball-dark-small.png').cl('black').w('70%')
    page.par('"Ridiculogram"').center().fr()
    
    page = p.page('Two kinds of troublesome networks')
    page.vspace('2em')
    page.h2('Network is too dense!').cl('h2yellow')
    page.par('We need to measure network characteristics, but our \
    network is too dense: high computational cost')
    page.vspace('2em')
    page.h2('Network contains too much noise!').cl('h2yellow')
    page.par('There is a meaningful core that is obscured by lots of noisy edges')
    
def get_section_sparsification(p):
    page = p.pagesection('First case')
    page = p.page('First case')
    page.par('We have a very <b>dense</b> matrix. It is the "correct" matrix, but its density makes\
    it hard to efficiently compute its network charachteristics such as its <b>community structure</b>.')
    page.par('Example:')
    l = page.ul()
    l.item('Large dense similarity matrix.')
    l.item('Dimensionality reduction.')
    l.item('Correlation matrix in <b>genetic</b> or <b>protein</b> interaction networks?')
    page.vspace('2em')
    page.h2('We need to approximate the graph').cl('h2yellow').fr()
    
    page = p.page('Dense similarity matrix')
    page.par('Find a sparse <b>approximation</b> of the original graph').center()
    page.video('5-anim.mp4', loop=True).w('80%').cl('white')
    page.vspace('0.5em')
    page.h2('Sparsification').cl('h2yellow').fr()
    
    page = p.page('Sparsification')
    page.par('There are a number of relevant methods:')
    page.vspace('2em')
    l = page.ul()
    i1=l.item('using <b>spanning trees</b>')
    u = i1.ul()
    u.item('Kelner, Jonathan A. and Madry, Aleksander, "Faster generation of random spanning \
    arXiv:0808.4134 [cs]  (2008). arXiv: 0808.4134').cl('reference')
    u.vspace('0.5em')
    i2 = l.item('using methods to preserve the <b>spectrum</b> of the Laplacian')
    u = i2.ul()
    u.item('Spielman, Daniel A. and Teng, Shang-Hua, "Spectral Sparsification of Graphs",\
    trees", in Foundations of Computer Science, 2009. FOCS 09. 50th Annual IEEE Symposium \
    on (IEEE, 2009), pp. 13--21.').cl('reference')
    u.vspace('0.5em')
    i3=l.item('using <b>expanders</b> in general')
    u = i3.ul()
    u.item('Goyal, Navin and Rademacher, Luis and Vempala, Santosh, "Expanders via random \
    spanning trees", in Proceedings of the twentieth Annual ACM-SIAM Symposium on Discrete \
    Algorithms (Society for Industrial and Applied Mathematics, 2009), pp. 576--585.').cl('reference')
    u.vspace('0.5em')
    
def get_section_pruning(p):
    p.pagesection('Second case')
    page = p.page('Second case')
    page.par('We have a network with a backbone of interest, thought to be obscured by lots\
    of noisy edges. ')
    page.par('The task is to throw away edges that are not <b>significant</b> and see what remains.')
    page.par('Example:')
    l = page.ul()
    l.item('Lexical networks: word co-occurrence networks')
    l.item('Co-authorship networks')
    page.c(1).w('50%').im('lexical-network.jpg').h('300px')
    page.c(2).w('50%').im('coauthorship.jpg').h('300px').center()
                
    page = p.page('Pruning')
    page.vspace('2em')
    page.h2('NOT an approximation problem').cl('h2yellow')
    page.vspace('2em')
    page.par('What graph property do we want to preserve as we remove edges?').center()
    page.par('Do we even want to do that?').center().fr()
    
    page = p.page('')
    page.par('Consider a network where edges have <b>integer</b> weights counting the number of some <b>event</b> \
        relating the end nodes.').center()
#     page.im('ohiostate-crop.pdf.png').cl('white').h('70%')
    page.im('occupations-sample.png').cl('white').w('100%')
    # p.page().im('MIT-crop.pdf.png').cl('white').h('80%')
    
    
    page = p.page('Pruning a dense weighted graph')
    page.par('How to get rid of less significant edges in a graph?').center()
    page.par('How to extract the most significant subgraphs from a weighted  graph?').center()
    page.vspace('2em')
    page.h2("<b>Weight thresholding isn't good enough</b>").cl('h2yellow').fr()

def get_section_MLF(p):    
    p.pagesection('Marginal Likelihood Filter')
    
    page = p.page('Statistical significance')
    page.par('We use the <b>Marginal Likelihood Filter</b>').center()
    page.im('unwindingthehairballgraph.png').w('80%')
    page.par('To appear in Physical Review E.').center().cl('reference')

    page = p.page('Statistical significance')
    page.par('Not all edges are created (statistically) equal').center()
    div = page.div().fr()
    div.im('significance1.svg').cl('white').w('80%')
    div.par('which bond is more <b>significant</b>?').center()
    

    page = p.page('Marginal Likelihood Filter (MLF)')
    page.par('Let $G$ be a graph with integer edge weights.')
    page.par('<b>Null Model:</b> Given the weighted degrees of the nodes, if everything else \
        were random, what would the edge weights look like?')
    l = page.ol()
    l.item('Take all the unit edges out of the graph, then "sprinkle" them back over the nodes!')
    l.item('Let each unit edge choose two nodes, each with probability proportional to its degree.')
    page.par('<b>MLF: </b> two nodes would be connected with probability \
        proportional to the <b>product</b> of their weighted degrees.')
    page.h3(r'$p=\frac{k_{i}k_{j}}{2T^{2}}, \,\,\, T=\frac{1}{2}\sum_{i}k_{i}$').center()
    page.h2('The Configuration Model*').center().fr()

    
    page = p.page('The filter')
    page.par('According to the null model').center()
    page.par('The weight of an edge follows a <b>binomial</b> distribution.').center()
    page.par(r'$\Pr\left[\sigma_{ij}=m\,|\,k_{i},k_{j},T\right] = {T \choose m}p^{m}(1-p)^{T-m}$').center()
    page.par('Given the null model, compute a p-value for each edge. Lower p-value \
        corresponds to higher significance.')
    page.im('binomials.svg').cl('white').h('30%')
    page.im('hierarchy.svg').cl('white').right().h('30%')
    
    page = p.page('Some details')
    page.h2('The p-value').cl('h2yellow')
    page.vspace('2em')
    page.par(r'$s_{ij}(w_{ij})=\sum_{m\geq w_{ij}}\Pr\left[\sigma_{ij}=m\,|\
    \,k_{i},k_{j},T\right]$').center().fontsize('1.5em')
    page.vspace('2em')
    page.par('compute using the <b>binomial test</b>.').center()
    page.par('e.g. in Python\'s <b>STATSMODELS</b> package').center()
    




def get_section_example1(p):
    
    page = p.page('Example:')
    page.par('The full occupations co-occurrence graph of Massachusetts:')
    page.im('massachusetts-ocupations-attorney-hairball-dark.png').cl('black').w('70%')
    
    page = p.page('Pruned using weight thresholding')
    page.par('3% truncation').fontsize('0.7em').center().w('auto').margin('10px')
    page.im('weight-newyork-occupation-truncated-3-pct-labels-adjusted-crop.svg ').cl('white').h('70%')
    
    page = p.page('Pruned using <b>MLF</b>')
    page.par('Again, 3% truncation').fontsize('0.7em').center().w('auto').margin('10px')
    page.im('MLF-newyork-occupation-truncated-100-pct-labels-adjusted-crop.svg').cl('white').h('70%')
    
    page = p.page('')
    page.im('MLF-newyork-occupation-truncated-100-pct-labels-adjusted-crop.svg').cl('white').h('90%')
    
def get_section_example2(p):

    p.pagesection('Another example')
    
    page = p.page('US air traffic network')
    page.par('Pruned using weight thresholding').center()
    page.par('15% truncation').fontsize('0.7em').center().w('auto').margin('10px')
    page.im('2012-passengers-new-plot-weight-filter-weight-15pct-separate.svg').cl('white').h('60%')
    
    page = p.page('US air traffic network')
    page.par('Pruned using <b>MLF</b>').center()
    page.par('15% truncation').fontsize('0.7em').center().w('auto').margin('10px')
    page.im('2012-combined-map-15pct-MLF.svg').padding('0.2em').h('70%').cl('white')
    
    
def get_section_discussion(p):
    p.pagesection('Discussion')
    
    page = p.page('Weight thresholding vs <b>MLF</b>')
    page.im('graph-measures-airports-alt.svg').w('80%').cl('white')

    page = p.page('Maximum entropy formulation')
    page.par('<b>Question:</b> If the only reliable information we had about the the network\
    was the expectation value of property $x$, then what would be expect from a random ensemble of graphs to look like?')
    page.vspace('1em')
    page.h2('Maximum entropy ensemble').cl('h2yellow').fr()
    page.vspace('1em')
    
    div = page.div().fr()
    div.par(r'<b>Alternatively,</b> what is the maximum entropy ensemble of graphs subject to the'+
              r' constraints $\left\langle x_1\right\rangle=c_1$, $\left\langle x_2\right\rangle=c_2$, $\cdots$?')
    div.vspace('1em')
    div.par(r'$P(G)\sim e^{\theta_{1}x_{1}(G)+\theta_{2}x_{2}(G)+\cdots\theta_{m}x_{m}(G)}$').center().fontsize('1.5em') 
    
    page = p.page('Maximum entropy formulation')
    page.par('Find the maximum entropy ensemble of graphs with the <b>degree sequence</b> equal to\
    that of the observed graph <b>on average</b>.')
    page.par(r'\[P(G)=\frac{1}{Z}g\left[\left\{ \sigma_{ij}\right\} \right]\exp\left[-\sum_{i < j}(\theta_{i}+\theta_{j})\sigma_{ij}\right]\,\,\,\forall G\in\mathscr{G}\]')
    page.par(r'Fit the parameters $\theta_i$ to the node degrees...').center()
    page.par(r'\[P(G)=\frac{1}{Z}\frac{\left(\sum_{i < j}\sigma_{ij}\right)!}{\prod_{i < j}\sigma_{ij}!}\prod_{i < j}\left(\frac{k_{i}k_{j}}{2T^{2}}\right)^{\sigma_{ij}}\,\,\,\forall G\in\mathscr{G}\]')
    page.vspace('1em')
    page.h2('Multinomial distribution').cl('h2yellow')
    
    page = p.page('Maximum entropy formulation')
    page.par('<b>Theorem:</b> When the joint probability distribution is multinomial, \
    the marginal probability distribution is binomial')
    page.vspace('2em')
    page.par('So, the distribution used in <b>MLF</b> is the marginal distribution of a \
    maximum entropy ensemble.')
    
    p.pagesection('If there is time...')
    
    page = p.page('Global Likelihood Filter')
    page.par('We can use the maximum entropy ensemble to compute a measure of significance for\
    each possible <b>subraph</b> and pick the most significant one.')
    page.vspace('1em')
    page.h2('GLF').cl('h2yellow')
    page.vspace('1em')
    li = page.c(1).w('60%').ul()
    li.item('NP-hard?')
    li.item('Requires Monte-Carlo methods')
    li.item('Two-tailed test')
    li.item('Results similar to <b>MLF</b> for moderate truncations')
    page.c(2).w('40%').im('MLF_vs_GLF-crop.svg').h('30%').cl('white')
    

def get_section_conclusion(p):
    p.pagesection('Conclusion')
    
    page = p.page('In conclusion...')
    page.vspace('1em')
    li = page.ul()
    li.item('We argued that <b>sparsification</b> and <b>pruning</b> are two different problems.')
    li.item('We introduced a statistical filter for pruning integer weighted networks: \
    <b>marginal likelihood filter</b>')
    li.item('<b>MLF</b> assumes that the most meaningful aggregate feature of the graph\
    is its degree sequence.')
    li.item('MLF is fast: nearly linear in the number of edges.')
    li.item('MLF is closely related to <b>maximum entropy</b> ensemble methods.')
    page.vspace('1em')
    page.par('<b>Question:</b> are these filters usefull in understanding biological networks\
    list genetic or protein interaction networks? ').fr()
    
    
    
    
    




p = Presentation(theme=ThemeDark(), width=1200, height=1024, margin='0.05', transition='fade', data_dir='./files/example/')



get_frontpage(p)
get_section_intro(p)
get_section_sparsification(p)
get_section_pruning(p)
get_section_MLF(p)
get_section_example1(p)
get_section_example2(p)
get_section_discussion(p)
get_section_conclusion(p)


p.endpage(url_qr = 'QR-paper-pruning.png')
p.export('presentation-example.html')
