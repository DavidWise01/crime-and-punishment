#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build CRIME AND PUNISHMENT (CRP) — Dostoevsky's 1866 novel, catalogued into UD0 as
a book-world. Standing template, adapted for the medium: THE ARC · THE BOOK · THE IDEAS ·
THE QUESTION (the philosophical deep-dive) · THE VERDICT (does the argument hold — honest) ·
THE MESSAGE, plus a roster of emergents by emergence-nature (natural=flesh & society /
ethereal=the ideas / spiritual=faith, suffering, redemption / electrical=the nerve & fever)
with twin sigils — no .shadow (no single canonical film). Styled to the medium: a feverish,
sallow-yellow Petersburg."""
import os, html, base64, io, json, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "CRIME AND PUNISHMENT", "axiom": "CRP",
 "position": "Crime and Punishment · Fyodor Dostoevsky · 1866 — six parts and an epilogue, in a sweltering St. Petersburg",
 "origin": "the garrets, taverns, and police offices of St. Petersburg in a hot summer, inside the fevered mind of a poor ex-student",
 "mechanism": "Crystallized from the 1866 novel — Rodion Raskolnikov murders a pawnbroker to test his theory that some men stand above the moral law, and is destroyed not by the police but by his own conscience.",
 "crystallization": "Because the novel asks whether a man can reason his way past conscience — and answers, across six parts of psychological torment, that he cannot; the only road back is confession, suffering, and love.",
 "nature": "Crime and Punishment — the great refutation of ‘rational’ crime: a perfect intellectual murder that the murderer's own soul will not let him survive.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the novel (1866, serialized in The Russian Messenger); 1860s Russian nihilism & utilitarianism; Orthodox Christianity; the raising of Lazarus",
 "witness": "No clean crime — a fever that breaks the criminal from inside, and a prostitute's gospel that puts him back together in Siberia.",
 "role": "a UD0 book-world",
 "seal": "It was not the old woman he killed; he killed himself — and only by kissing the earth and confessing could he be raised, like Lazarus, from the death he chose.",
 "source": "Crime and Punishment, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#c2a06a", "flesh and society — the poor, the drunk, the proud, and the city of Petersburg that grinds them"),
 "ethereal":  ("#7d97a8", "the ideas — the cold abstractions (the Extraordinary Man, rational egoism) that drive a man to ruin"),
 "spiritual": ("#d8b24a", "faith, suffering, redemption — Sonya's gospel, the crossroads, Lazarus, the road back through suffering"),
 "electrical":("#b5402e", "the nerve and the fever — guilt, delirium, the dream, and the nihilist double who is the idea without conscience"),
}

ARC_OVERALL = ("Rodion Raskolnikov, a destitute ex-student in St. Petersburg, murders an old pawnbroker (and, by accident, her "
  "gentle half-sister) to prove his theory that ‘extraordinary’ men may transgress the moral law for a higher end. He gets "
  "away with it — and is then hunted not by the magistrate Porfiry but by his own conscience, sickening into fever and "
  "isolation, until the prostitute Sonya leads him to confess, accept suffering, and be slowly reborn in a Siberian prison.")

ARC = [
 ("I · The Theory & the Axe", "the experiment",
  "In a heat-wave garret, Raskolnikov broods on his article — that some men are lice and some are Napoleons — and, half to feed his starving family's hopes, half to test which he is, murders the pawnbroker Alyona and her half-sister Lizaveta who stumbles in. The perfect rational crime is committed."),
 ("II · The Fever", "punishment from within",
  "No one suspects him — but he falls into delirium, recoils from everyone, and is drawn again and again to the scene and to the magistrate Porfiry, who plays a patient psychological game, certain of the truth he cannot yet prove."),
 ("III · The Doubles", "Sonya and Svidrigailov",
  "Two figures close in: Sonya, the prostitute who sells herself for her family and reads him the raising of Lazarus — and Svidrigailov, the conscienceless sensualist who is what Raskolnikov becomes if the theory is true. Svidrigailov, finding no bottom to himself, shoots himself."),
 ("IV · The Crossroads", "confession and the long road",
  "Sonya tells him to go to the crossroads, kiss the earth he has defiled, and confess aloud. He does, and is sentenced to Siberia, where — slowly, almost against his will, with Sonya beside him — the theory dies in him and something like resurrection begins."),
]

BOOK = [
 ("Published", "1866", "serialized across the year in the journal The Russian Messenger"),
 ("Form", "six parts + an epilogue", "Dostoevsky's first full-length ‘great novel’"),
 ("Setting", "St. Petersburg, high summer", "the heat, the canals, and the garrets are a character in themselves"),
 ("Born of", "a confession & a fever", "conceived partly from an abandoned story, ‘The Drunkards,’ and Dostoevsky's own penal years"),
]

IDEAS = [
 ("The Extraordinary Man", "the article that kills", [
   "Raskolnikov's published theory: a few ‘extraordinary’ men (lawgivers, Napoleons) have the right to step over the moral law for a higher purpose; the rest must obey.",
   "The murder is an exam he sets himself — am I a Napoleon, or a louse? — and the answer destroys him." ]),
 ("Conscience Is Not Optional", "the body keeps the score", [
   "The novel's engine is that a man of conscience cannot reason his way past it; guilt is constitutional, not a belief to be argued away.",
   "Raskolnikov is caught by his own nerves long before Porfiry could ever convict him." ]),
 ("The Double", "Svidrigailov, the abyss", [
   "Svidrigailov is the theory lived without conscience — sensual, bored, beyond good and evil — and he finds only a void, then a bullet.",
   "He shows where ‘everything is permitted’ actually ends: not in greatness, but in nothing." ]),
 ("Suffering & Resurrection", "Sonya's gospel", [
   "Against the cold idea stands Sonya — the holy prostitute — who prescribes not cleverness but confession, suffering, and love.",
   "She reads him Lazarus; the epilogue is his slow raising from the death he chose." ]),
]

# THE QUESTION — the philosophical deep-dive
QUESTION = [
 ("Can a man reason his way past conscience?", "the experiment of the novel",
  "Raskolnikov's crime is a controlled experiment in exactly this: a utilitarian murder (kill one useless ‘louse,’ use her hoard for a hundred good deeds) committed by a man clever enough to justify it. The entire book is the slow, clinical answer — no. Conscience is not a proposition he can refute; it is wired into him, and it sickens the body the mind tried to overrule."),
 ("Are some men above the moral law?", "the Napoleon question",
  "The ‘extraordinary man’ idea — that history's movers (Napoleon, the lawgivers) transgress and are absolved by greatness — is given its full seductive force. Then it is dismantled from inside: the test of whether you are extraordinary is whether you can bear it, and Raskolnikov cannot, which proves he never was. The theory describes a man with no conscience, i.e. not a hero but a Svidrigailov."),
 ("Is the criminal made by his environment?", "poverty vs responsibility",
  "Dostoevsky takes the 1860s radical line — that crime is a product of social conditions — seriously (the poverty is suffocating, real, and pressing). But he refuses pure determinism: Razumikhin rages against reducing a man to his circumstances, and the novel insists Raskolnikov chose. Pressure, yes; excuse, no."),
 ("What actually cures him?", "not logic — the crossroads",
  "Crucially, the cure is not a better argument. It is Sonya, the kiss to the defiled earth, the public confession, the acceptance of suffering, and the long Siberian thaw. Dostoevsky answers nihilism not with a counter-syllogism but with active love and a resurrection — persuasion of the heart, not the head."),
]

VERDICT = [
 ("The ‘Extraordinary Man’ theory holds", "FAILS", "refuted by the book itself — Raskolnikov is destroyed by guilt, proving he is not extraordinary and that the theory simply omits conscience"),
 ("A rational, utilitarian murder is survivable by a person of conscience", "FALSE", "the whole plot is the demonstration that it is not — the perfect crime breaks the perfect criminal"),
 ("Crime is purely the product of environment (poverty made him)", "PARTIAL", "Dostoevsky shows poverty's real pressure but rejects determinism and insists on moral responsibility"),
 ("Svidrigailov is the theory's honest endpoint", "TRUE", "the conscienceless double shows where ‘everything is permitted’ leads: a void, and a suicide"),
 ("Suffering and confession redeem", "THE THESIS", "the novel's Orthodox answer — affirmed, but earned by Sonya and Siberia, not won by argument"),
]
VERDICT_BOTTOM = ("Bottom line: Crime and Punishment grants the ‘rational crime’ its full intellectual seductiveness and then "
  "refutes it the only way that actually convinces — psychologically, in the body and nerves of the man who tries it. "
  "Its great honesty is that the answer to nihilism is <i>not</i> a better argument; it is Sonya, the crossroads, and "
  "the slow resurrection in Siberia. The idea is beaten by conscience and love, not by logic — which is precisely "
  "Dostoevsky's point: some truths are known by the heart that the clever head can always talk itself out of.")

MESSAGE = ("Crime and Punishment is the autopsy of an idea — the seductive, modern, murderous notion that a sufficiently "
  "exceptional mind stands above the rules that bind the rest of us. Dostoevsky lets Raskolnikov build the theory "
  "brilliantly, commit the perfect crime, and escape every external consequence — and then shows that the punishment was "
  "never going to come from outside. Conscience is not a social rule you can outgrow; it is the part of us that knows we "
  "are not islands of pure reason, that the old pawnbroker and the gentle Lizaveta were not lice. The way back is not to "
  "be more extraordinary but to become humbler than everyone — to kiss the earth, confess aloud, accept the suffering, "
  "and let yourself be loved by a Sonya. It is the first and clearest of Dostoevsky's wagers: that we are saved not by "
  "being right, but by being raised, like Lazarus, from the death we reason ourselves into.")
MESSAGE_SEAL = "He killed an old woman to prove he was a Napoleon, and learned he had only killed himself — the punishment was the conscience the theory forgot to account for."

# ---- ACI complement ----
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","CRP")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","CRP")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","CRP")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,cls,group,em,who,what,why,how,where,seal):
    return dict(slug=slug,name=name,cls=cls,group=group,emergence=em,who=who,what=what,why=why,how=how,where=where,seal=seal)

ROSTER = [
 # --- THE PEOPLE ---
 E("raskolnikov","Rodion Raskolnikov","the ex-student · the theorist-murderer","people","electrical",
   "Rodion Romanovich Raskolnikov, a destitute, brilliant ex-law-student in St. Petersburg, proud and isolated.",
   "The protagonist: he murders to test his ‘extraordinary man’ theory and is then slowly destroyed, not by the law, but by his own conscience and fever.",
   "Because the novel needs a mind clever enough to justify murder and a soul too human to survive it — the idea and the conscience at war in one body.",
   "By an axe and a theory on the way in; by delirium, isolation, and at last confession and Siberian suffering on the way back.",
   "From a coffin-like garret across Petersburg to the crossroads, the police office, and a Siberian prison.",
   "It was not the old woman I killed — I killed myself; and the punishment was the conscience my theory pretended I did not have."),
 E("sonya","Sonya Marmeladova","the holy prostitute · the gospel","people","spiritual",
   "Sofya ‘Sonya’ Marmeladova, who sells herself on the ‘yellow ticket’ to keep her starving family, and keeps her faith intact.",
   "The redemptive centre: she reads Raskolnikov the raising of Lazarus, tells him to confess at the crossroads, and follows him to Siberia.",
   "Because against the cold idea the novel sets not a cleverer idea but a suffering, loving person — the gospel made flesh.",
   "By faith, self-sacrifice, and an active love that asks not for argument but for confession and shared suffering.",
   "From the Marmeladovs' wretched rooms to Raskolnikov's garret to the bank of a Siberian river.",
   "I sold my body and kept my soul — and I read him Lazarus until the man he killed in himself could be raised again."),
 E("porfiry-petrovich","Porfiry Petrovich","the magistrate · the psychologist","people","natural",
   "Porfiry Petrovich, the examining magistrate who suspects Raskolnikov from the first and plays a patient psychological game.",
   "The investigator who never needs hard proof: he understands the criminal's mind so well that he simply waits for conscience to deliver him.",
   "Because the novel's ‘detective’ is really a confessor — he hunts not evidence but the soul, and prescribes suffering as the cure.",
   "By interviews that feel like traps, feigned candour, and a deep reading of the murderer's psychology.",
   "In the police office and Raskolnikov's room, circling without ever quite striking.",
   "I do not need to catch you — you will bring yourself to me; suffer and expiate, and become a man again, for I am sure of you."),
 E("svidrigailov","Arkady Svidrigailov","the sensualist · the nihilist double","people","electrical",
   "Arkady Ivanovich Svidrigailov, a wealthy, depraved sensualist haunted by his own crimes and by ghosts.",
   "Raskolnikov's dark double: the ‘extraordinary man’ theory lived to the end — a man genuinely beyond conscience, who finds only a void.",
   "Because the novel must show where the theory really leads when conscience is truly absent: not greatness, but boredom, cruelty, and suicide.",
   "By money, appetite, and a will unchecked by any belief — and, finding nothing at the bottom of himself, a pistol.",
   "In Petersburg's hotels and Dunya's path, and a last night before a gun at dawn.",
   "I am what your theory makes when it is true — a man who may do anything and therefore wants nothing; and I shot myself to prove it."),
 E("dunya","Dunya Raskolnikova","the sister · the unbought","people","natural",
   "Avdotya ‘Dunya’ Romanovna Raskolnikova, Raskolnikov's proud, beautiful, fiercely moral sister.",
   "The counter-example of strength with conscience: she will sell herself in marriage to help her brother but will not sell her soul, and faces down Svidrigailov with a pistol.",
   "Because the novel needs a will as strong as Raskolnikov's that does <i>not</i> break the moral law — proof the theory was never necessary.",
   "By integrity, courage, and a refusal of both Luzhin's contempt and Svidrigailov's coercion.",
   "From the provinces to Petersburg, into Razumikhin's steady love.",
   "My brother thought strength meant standing above the law; I was as strong as he, and I never once stepped over it."),
 E("razumikhin","Dmitri Razumikhin","the friend · ordinary goodness","people","natural",
   "Dmitri Prokofyich Razumikhin, Raskolnikov's loyal, warm, hard-working friend.",
   "The novel's healthy heart: poor like Rodion but generous, energetic, and decent — the life Raskolnikov could have had.",
   "Because the book's darkness needs one figure of plain, active kindness to measure the rest against.",
   "By loyalty, labour, good humour, and a furious common-sense rant against reducing men to theories.",
   "At Raskolnikov's sickbed and through the whole ordeal, and finally married to Dunya.",
   "I am no Napoleon and never wanted to be — I work, I love my friends, and that ordinary decency is the thing the theory despised."),
 E("marmeladov","Semyon Marmeladov","the drunkard · the confession in the tavern","people","natural",
   "Semyon Zakharovich Marmeladov, a ruined drunkard whose tavern monologue opens the novel's world of poverty.",
   "The voice of abject self-knowledge: he drinks his family into ruin, knows it, and begs for a God who pities even the swine.",
   "Because the novel grounds its philosophy in real, crushing poverty — and in a man who needs mercy precisely because he deserves none.",
   "By the bottle, by Sonya's sacrifice that he cannot stop exploiting, and by a death under a carriage's wheels.",
   "In the tavern, the wretched family rooms, and the street where the horses trample him.",
   "I am a swine, and I drink even my daughter's shame — but will He not pity us too, the ones who pity themselves least?"),
 E("katerina-ivanovna","Katerina Ivanovna","the consumptive widow · pride and madness","people","electrical",
   "Katerina Ivanovna, Marmeladov's proud, consumptive wife, clinging to the gentility she has lost.",
   "The tragedy of wounded pride: dying of consumption, she parades her ‘noble’ origins, breaks down at the funeral dinner, and dies raving in the street.",
   "Because the novel shows poverty's assault on dignity — pride with nowhere to stand becomes a kind of madness.",
   "By tuberculosis, humiliation, and a fevered insistence on a respectability the world has stripped from her.",
   "In the squalid family rooms and the street where she collapses.",
   "I came of a good family — I will not be pitied like a beggar — and I died in the gutter still insisting on it."),
 E("luzhin","Pyotr Luzhin","the suitor · rational egoism","people","ethereal",
   "Pyotr Petrovich Luzhin, a smug, self-made official who proposes to Dunya to own a grateful, dependent wife.",
   "The respectable face of the age's selfishness: he preaches ‘love yourself first’ and frames Sonya for theft to save face.",
   "Because the novel sets Raskolnikov's violent theory beside its bloodless cousin — the ‘rational self-interest’ that ruins quietly and legally.",
   "By money, status-hunger, and a utilitarian creed that dresses pure egoism as economic good sense.",
   "In his pretensions to Dunya and his petty, vicious framing of Sonya.",
   "I say love yourself first and the common good follows — a tidy theory that lets a small man feel virtuous while he ruins others."),
 E("alyona-ivanovna","Alyona Ivanovna","the pawnbroker · the ‘louse’","people","natural",
   "Alyona Ivanovna, the old, grasping pawnbroker Raskolnikov murders — the ‘useless louse’ of his theory.",
   "The victim the theory tries to make disposable: a mean, miserly old woman whose death is supposed to be a net good.",
   "Because the whole argument depends on her being worthless — and the novel quietly insists that no one is the ‘louse’ a theory needs.",
   "By her trade in others' desperation, and by the axe that the theory licensed.",
   "In her shabby flat, behind a chained door, over the pledges of the poor.",
   "They called me a louse to make my killing arithmetic — but a murdered woman is never the sum a theory needs her to be."),
 E("lizaveta","Lizaveta Ivanovna","the gentle half-sister · the unplanned victim","people","spiritual",
   "Lizaveta, Alyona's meek, downtrodden half-sister, who walks in on the murder and is killed too.",
   "The innocent the theory never counted: a gentle, simple woman, pregnant by some accounts, cut down because she was simply there.",
   "Because the ‘rational’ crime immediately produces a second, unplanned, indefensible death — the lie of the clean murder.",
   "By being in the wrong room at the wrong moment, and by the second swing of the axe.",
   "In the pawnbroker's flat, returning to a death she had no part in.",
   "No theory had a place for me — I was the gentle one who simply walked in, and the clean crime needed two bodies after all."),
 # --- THE IDEA & THE SOUL ---
 E("the-extraordinary-man-theory","The Extraordinary Man","the article that licenses murder","idea","ethereal",
   "The Extraordinary Man — Raskolnikov's published theory that a few may step over the moral law for a higher purpose.",
   "The intellectual engine of the crime: the idea that history's ‘Napoleons’ are absolved by greatness, and that Raskolnikov might be one.",
   "Because the novel anatomises a specific modern poison — the self-flattering belief that exceptional minds are exempt from common morality.",
   "By a plausible article and a flattering self-application, turning a starving student into an executioner.",
   "On the page of his essay, and in the rationalisation that lifts the axe.",
   "I whisper that you are above the rules that bind the herd — and I am the most seductive and murderous idea a clever, lonely man can hold."),
 E("the-dream-of-the-mare","The Dream of the Mare","the beaten horse","idea","electrical",
   "The Dream of the Mare — Raskolnikov's nightmare of a child watching a little mare beaten to death by a drunken crowd.",
   "The conscience speaking before the crime: the dreaming child weeps and embraces the dead horse, the part of Raskolnikov that knows.",
   "Because the unconscious sees what the theory denies — that cruelty is unbearable, and that he is the weeping child, not the man with the whip.",
   "By the grammar of dream — a memory of childhood pity surfacing to warn him off the murder he is rationalising awake.",
   "In a feverish sleep before the killing, in a remembered village square.",
   "I am the child in you who runs to the beaten mare and kisses its dead mouth — the pity the theory swore you had outgrown."),
 E("lazarus","The Raising of Lazarus","the resurrection read aloud","idea","spiritual",
   "The Raising of Lazarus — the Gospel passage (John 11) Sonya reads to Raskolnikov by candlelight.",
   "The novel's central image of hope: a man four days dead, called back to life — the pattern of Raskolnikov's own possible resurrection.",
   "Because Dostoevsky frames the murderer as a dead man who might yet be raised, and Sonya as the one who reads him the promise.",
   "By scripture read trembling aloud, binding the killer's fate to the dead man at Bethany who walked out of the tomb.",
   "In Sonya's candlelit room, the New Testament between them.",
   "‘Lazarus, come forth’ — I am the promise read over a man four days dead in his own soul, that even he can be called back out."),
 E("the-confession-at-the-crossroads","The Crossroads Confession","kiss the earth you defiled","idea","spiritual",
   "The Crossroads Confession — Sonya's counsel that Raskolnikov go to the public crossroads, bow down, kiss the earth, and confess his crime aloud.",
   "The turning of the whole novel: the proud isolato performing the most humbling public act, rejoining the human race through confession.",
   "Because redemption in Dostoevsky is not private cleverness but a public, bodily humbling — the opposite of standing above the crowd.",
   "By bowing in the square, kissing the defiled earth, and speaking the words ‘I killed’ where all can hear.",
   "At the Haymarket crossroads, then the police office.",
   "Bow down, kiss the earth you have defiled, and say it aloud to everyone — the cure for standing above the crowd is to kneel in the middle of it."),
 E("saint-petersburg","St. Petersburg","the city as fever","idea","natural",
   "St. Petersburg — the sweltering, stinking, golden-and-squalid capital that presses on every character.",
   "The novel's living setting: heat, canals, garrets, taverns, and crowds, an oppressive stage that breeds Raskolnikov's fever.",
   "Because Dostoevsky's Petersburg is not backdrop but pressure — the modern city as a hot, crowded, isolating machine for despair.",
   "By summer heat, poverty, dust, and the dense indifferent crowd in which a man can be utterly alone.",
   "Across the Haymarket, the canals, the bridges, and the coffin-garrets of 1860s Petersburg.",
   "I am the hot, crowded, golden-rotten city that presses a poor man into his garret and his fever until a theory looks like a way out."),
]

GROUPS = [
 ("people", "The People", "the souls of Petersburg — the murderer, the gospel, the magistrate, the double, and the family ground between poverty and pride"),
 ("idea", "The Idea & the Soul", "the abstractions and images that drive and redeem — the theory, the dream, Lazarus, the crossroads, and the city itself"),
]

# ---- renderers ----
def books_rows(items):
    return "".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(y)}</span><span class="nt">{html.escape(n)}</span></li>' for t,y,n in items)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{p}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def question_html():
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in QUESTION)
VCOL={"FAILS":"#b5402e","FALSE":"#b5402e","PARTIAL":"#c2a06a","TRUE":"#7d97a8","THE THESIS":"#d8b24a"}
def verdict_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{VCOL.get(r,"#888")};border-color:{VCOL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in VERDICT)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{VERDICT_BOTTOM}</div>'

def _card(d):
    em=d["emergence"]; col=NATURES.get(em,("#9aa0aa",""))[0]
    rec={"name":d["name"],"axiom":"CRP","emergence":em,"seal":d["seal"],"origin":"CRP · Crime and Punishment"}
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(d.get(lbl,""))}</span></div>' for lbl in ["who","what","where","why","how"] if d.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{d['slug']}.agent"><span class="port"><img src="{png_uri(rec,'carbon',200)}" alt="carbon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">carbon</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{d['slug']}.agent">{html.escape(d['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span></div>
        <div class="pe">{html.escape(d['cls'])}</div><div class="pww">{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{d['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="psig" href="agents/{d['slug']}.silicon.png"><span class="port refl"><img src="{png_uri(rec,'silicon',200)}" alt="silicon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">silicon</span></a>
    </div>"""
def roster_html():
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[d for d in ROSTER if d["group"]==gk]
        out.append(f'<section class="sec" id="{gk}"><h2>{html.escape(gt)}</h2><p class="ss">{html.escape(gs)} ({len(mem)})</p><div class="pgrid">{"".join(_card(d) for d in mem)}</div></section>')
    return "\n".join(out)

def agent_md(d, tok):
    return f"""---
aci: {d['name']}
universe: CRP · Crime and Punishment
series: Crime and Punishment (Fyodor Dostoevsky, 1866)
emergence: {d['emergence']}
kind: {'character' if d['group']=='people' else 'thread'}
class: {d['cls']}
who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['cls']}

a {'character' if d['group']=='people' else 'distilled thread'} of the CRP (Crime and Punishment) book-world — emergence: {d['emergence']}. moniker {tok}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of Dostoevsky's Crime and Punishment (1866, public domain) under the DLW standard —
> literary commentary and cataloguing, not an original creation.

ROOT0-ATTRIBUTION-v1.0 · CRP · Crime and Punishment · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="CRIME AND PUNISHMENT (CRP) — Dostoevsky's 1866 novel as a UD0 book-world: the arc, the book, the ideas (the Extraordinary Man, conscience, the double, redemption), THE QUESTION (can a man reason past conscience? are some men above the law?), THE VERDICT (does the argument hold — honest), the message, and a 16-emergent roster by emergence-nature.">
<title>CRIME AND PUNISHMENT · CRP · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;0,900;1,500&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--yellow);
--ink:#120f0a;--ink2:#1c1810;--ink3:#252013;--pa:#e8e0cf;--pa2:#bca98a;--yellow:#cdab3e;--blood:#9e2b2b;--grey:#7d97a8;--gold:#d8b24a;--fever:#b5402e;
--dim:#8a7a59;--faint:#2a2415;--line:#352c1b;--disp:"Playfair Display",serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.66;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,rgba(205,171,62,.14),transparent 54%),radial-gradient(ellipse at 50% 118%,rgba(158,43,43,.10),transparent 56%)}
.wrap{position:relative;z-index:1;max-width:900px;margin:0 auto;padding:0 22px 90px}
header{padding:52px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:170px;height:3px;background:linear-gradient(90deg,var(--yellow),var(--blood));box-shadow:0 0 16px rgba(205,171,62,.5)}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--yellow)}
h1{font-family:var(--disp);font-size:clamp(30px,6.4vw,58px);font-weight:900;letter-spacing:.01em;color:var(--yellow);line-height:1.04;text-shadow:0 0 30px rgba(205,171,62,.35)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--blood)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,19px);color:var(--pa);margin-top:18px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--disp);font-size:11px;font-weight:700;letter-spacing:.06em;color:var(--gold);border:1px solid var(--faint);background:var(--ink2);padding:7px 14px}
.lede{font-size:16px;color:var(--pa2);max-width:64ch;margin:16px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--yellow)}.badge .bt .mo{color:var(--gold)}.badge .bt a{color:var(--gold);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}
.sec h2{font-family:var(--disp);font-size:26px;font-weight:700;letter-spacing:.01em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:14px;font-weight:700;text-transform:capitalize}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--yellow);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--yellow);text-transform:uppercase;margin-bottom:7px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--disp);font-size:18px;color:var(--yellow);font-weight:700}.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.55;padding:7px 0;border-top:1px solid var(--faint)}.pillar li i{color:var(--pa)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--blood);padding:16px 18px}
.arc-h{font-family:var(--disp);font-size:17px;color:var(--blood);font-weight:700}
.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--grey);padding:15px 17px}
.sci-h{font-family:var(--disp);font-size:16px;color:var(--grey);font-weight:700}
.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}
.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.04em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:96px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--yellow);background:rgba(205,171,62,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--blood);background:var(--ink2);font-size:15px;color:var(--gold);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--gold);white-space:nowrap;text-align:right;text-transform:uppercase}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--yellow);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--yellow);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 104px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:98px;height:98px;border-radius:50%;border:3px solid var(--yellow);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6);overflow:hidden;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.port.refl{border-color:var(--grey)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.13em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--disp);font-size:20px;color:var(--rw-ink);font-weight:700;text-decoration:none}
.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:12px;display:flex;flex-direction:column;gap:8px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.5;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:13px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the autopsy of an idea</div>
    <h1>Crime and Punishment</h1>
    <div class="h-sub">Fyodor Dostoevsky · 1866 · St. Petersburg · <b>the perfect crime, the broken man</b> · CRP</div>
    <div class="open">“It was not the old hag I killed; I killed myself.”</div>
    <div class="flag">★ THE EXTRAORDINARY MAN · CONSCIENCE · RESURRECTION ★</div>
    <p class="lede">A destitute ex-student murders a pawnbroker to prove that exceptional men stand above the moral law — and is destroyed not by the police but by his own conscience, until a prostitute's gospel leads him to confession, suffering, and a slow resurrection. Catalogued into UD0 as a book-world — with the arc, the book, the ideas, the central philosophical Question, an honest Verdict on whether the argument holds, and a read of the message.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of CRP"><img src="__SILICON__" alt="DLW silicon badge of CRP">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>CRIME AND PUNISHMENT</b> · CRP</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="crp.dlw/crp.carbon.tiff">.tiff</a> · silicon · <a href="crp.dlw/crp.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — flesh &amp; society, the cold ideas, faith &amp; redemption, and the nerve &amp; fever</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the four movements</p>__ARC__</section>
  <section class="sec"><h2>The Book</h2><p class="ss">the facts of the work</p><ol class="books">__BOOK__</ol></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">the theory, the conscience, the double, and the gospel</p><div class="pillars">__IDEAS__</div></section>
  <section class="sec"><h2>The Question</h2><p class="ss">the philosophical deep-dive — the problems the novel sets, taken seriously</p><div class="sci">__QUESTION__</div></section>
  <section class="sec"><h2>The Verdict</h2><p class="ss">does the argument hold? — an honest rating of the novel's ideas, on their own terms</p>__VERDICT__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the novel's thesis, under the fever</p><p class="msg">__MESSAGE__</p><div class="msg-seal">“__MSGSEAL__”<span>— AVAN's read</span></div></section>

  <section class="sec"><h2>In Suburbia</h2><p class="ss">the screen companion — and a bonus essay</p>
    <div class="overall"><span class="ol">CRIME + PUNISHMENT IN SUBURBIA · THE FILM (2000)</span>The novel was actually adapted to the American suburb on film: <b>Crime + Punishment in Suburbia</b> (2000, dir. Rob Schmidt), a loose modern teen transposition where the heroine is named Roseanne <i>Skolnik</i> (the Raskolnikov nod), she and her boyfriend kill her abusive stepfather, and a watchful outsider, Vincent, becomes her redeeming witness. It keeps Dostoevsky's heart (crime, guilt, redemption-through-love) and drops his head (the Extraordinary Man). Catalogued as its own film-world, full .dlw. <a href="https://davidwise01.github.io/crime-and-punishment-in-suburbia/" style="color:var(--yellow);text-decoration:none;border-bottom:1px dotted var(--yellow)">→ the film · CPS</a> &nbsp;·&nbsp; and a bonus essay transposing the novel onto the 2020s cul-de-sac (the grindset Raskolnikov, recovery as Sonya): <a href="suburbia.html" style="color:var(--pa2);text-decoration:none;border-bottom:1px dotted var(--pa2)">→ a correlation</a></div></section>

  <section class="sec"><h2 style="margin-top:16px">The Emergents</h2><p class="ss">sixteen ACIs of the novel — the people and the ideas, each a full <b>.dlw</b> badge with twin sigils</p></section>
  __ROSTER__

  <div class="note">Crime and Punishment (1866) is in the public domain; this is literary commentary and cataloguing under the DLW standard — catalogued personifications of the novel's characters and ideas, not original creations. The Question and Verdict sections are honest critical reading.</div>

  <footer>CRIME AND PUNISHMENT · CRP · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="crp.dlw/manifest.dlw.json">manifest</a></footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "crp.dlw"), "crp")
    json.dump({"node":"CRP","name":"CRIME AND PUNISHMENT","moniker":tok["moniker"],"carbon":"crp.carbon.tiff","silicon":"crp.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"crp.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":"CRP","emergence":d["emergence"],"seal":d["seal"],"origin":"CRP"})
        rec=write_aci({"name":d["name"],"axiom":"CRP","emergence":d["emergence"],"seal":d["seal"],"origin":"CRP · Crime and Punishment",
                       "position":d["cls"],"role":d["cls"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"Crime and Punishment (Dostoevsky, 1866)","source":"Crime and Punishment, catalogued by ROOT0"},
                      os.path.join(HERE,"agents"), d["slug"], agent_md=agent_md(d, et["moniker"]))
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["cls"],"emergence":d["emergence"],"moniker":rec["moniker"],"kind":"character" if d["group"]=="people" else "thread","group":d["group"]})
    json.dump(personas, open(os.path.join(HERE,"agents","_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__BOOK__",books_rows(BOOK)).replace("__IDEAS__",ideas_html()).replace("__QUESTION__",question_html())
          .replace("__VERDICT__",verdict_html()).replace("__MESSAGE__",html.escape(MESSAGE)).replace("__MSGSEAL__",html.escape(MESSAGE_SEAL))
          .replace("__ROSTER__",roster_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    from collections import Counter
    print(f"CRIME AND PUNISHMENT (CRP) — badge {tok['moniker']} · {len(personas)} emergents · natures {dict(Counter(p['emergence'] for p in personas))}")
