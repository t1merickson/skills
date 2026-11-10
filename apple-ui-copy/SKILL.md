---
name: apple-ui-copy
description: "Use when writing or reviewing user-facing text in an Apple-platform app or game: button and menu labels, alert titles and bodies, error messages, empty states, settings labels, placeholder text, notifications, permission purpose strings, onboarding, feature and control names, and VoiceOver descriptions. Also use when deciding capitalization for any UI string. Do not use for marketing copy, App Store listings, documentation prose, or general web UX writing with no Apple platform involved."
---

# Writing UI copy for Apple platforms

Apple publishes real rules for user-facing text, and most of them are mechanical enough to check. The Apple Style Guide states the obligation directly: developers and third-party developers should follow its guidelines for user-facing text.

Two layers, and they answer different questions:

- **Judgment layer.** Voice, tone, what to cut, what to call things. Apple gives procedures for these, not verdicts.
- **Mechanical layer.** Capitalization, ellipses, alert structure, specific banned words. These have right answers. Getting them wrong is a defect, not a style disagreement.

Weight your effort toward the mechanical layer. It is where copy is most often wrong and most easily fixed.

When a specific component matters, check the current Human Interface Guidelines page for that component rather than trusting recall. Apple revises these pages several times a year.

## Voice and tone

Voice is fixed across the app. Tone changes with the situation.

Apple describes its own voice as four qualities: **clarity, simplicity, friendliness, helpfulness**. Yours will differ, but pick about four and write them down.

The useful part is the procedure. Treat each quality as a dial, and set the balance per situation before writing:

| Situation | Turn up | Turn down |
|---|---|---|
| Celebrating an achievement | Friendliness, clarity about what was earned | Simplicity, helpfulness |
| Blocking error, user needs to act | Helpfulness, clarity | Friendliness, simplicity |
| Introducing a new feature | Clarity, friendliness, helpfulness | Simplicity |
| Serious health or security information | Clarity | Friendliness |

Never turn a quality all the way down. You are adjusting a balance, not switching modes.

**Simplicity and friendliness pull against each other.** Every word you add for warmth costs brevity. That trade is the actual decision, so make it deliberately rather than defaulting to "shorter is better."

**Clarity outranks everything, including the rule against repetition.** Apple's own no-connectivity alert repeats the word "data" twice in one sentence ("Turn on cellular data or use Wi-Fi to access data") because clarity mattered more than elegance. Do the same when the choice arises.

Do not use exclamation points except in genuinely celebratory moments. They look silly in quantity and they make light of bad news.

## Cut before you polish

### Remove fillers

Four categories, all of which Apple names:

- **Adverbs**: easily, quickly, simply, just
- **Adjectives**: fast, simple, easy
- **Interjections**: oops, uh-oh, oh no, hooray
- **Pleasantries**: sorry, thank you, please

The argument is not brevity. It is that these words **assert something about the user's situation that you cannot know**. Apple's example: an app that said "Simply enter your license plate number to quickly pay for parking." The writer, in a rental car with no signal, had to walk back to the car for the plate number and then walk away again to get service. It was neither simple nor quick. Cut to "Enter your license plate number to pay for parking" and nothing is lost.

The same logic condemns "oops" in an error (it signals you are not taking the problem seriously) and "we're sorry" in an alert (it reads as insincere and displaces the actual message).

Keep a descriptive word when it carries a fact that distinguishes the feature. "Feed your pets **automatically** when you're away" keeps "automatically" because scheduling is the whole point.

Treat stray exclamation points as filler punctuation. "They'll be there in 10 short minutes!" makes light of someone's delay.

### Remove repetition

Repetition is filler wearing a different coat. If the headline and the body say the same thing, collapse them.

Before: "Uh oh. We're running late." / "We're sorry, your delivery driver won't make it on time. They'll be there in 10 short minutes! Check the app for your driver's location."

After: "Delivery delayed 10 minutes." / "Check the app for your driver's location."

### Lead with the why

Put the benefit at the front of the sentence. The shape is: to get one thing, first do another thing.

- "Enter your phone number to get reservation updates" becomes "To get reservation updates, enter your phone number."

This matters most in error messages, notifications, and instructional copy, where people decide whether to keep reading from the first few words.

## Naming features, controls, and labels

Three criteria. A name does not have to pass all three, but you should know which one you are trading away.

1. **Belongs.** Fits the vocabulary already in your interface and the other things you have named.
2. **Sets expectations.** People predict what they will find before they tap. Deliver on the prediction and you build trust.
3. **Works everywhere.** Across languages, regions, platforms, and contexts.

Rules that follow from those:

**Use a verb when the feature is something people do.** A verb puts the person in control. Apple's own chain: "Vocal Isolation" is an audio engineering term describing the technology, "Isolate Vocals" is better because it is a verb, and "Enhance Dialogue" is best because it names both what changes and who it is for.

**Test a label against its worst-case value, not its typical one.** "Spending Power" reads fine at $500 and becomes a judgment at $0. Any label bound to data needs this check.

**Say it out loud in a sentence you would actually say.** Drop the candidate into "Hey, check out ___" or "just search for ___". "Let me check my Current Funds" fails immediately. "Balance" wins, because in a financial context the boring industry-standard word buys clarity and trust that brand expression does not.

Three registers are all legitimate: descriptive (Enhance Dialogue), emotional (Memories, where the clarity comes from emotion rather than explanation), and coined (AutoMix, which earns its clarity from parts people already understand). Pick by context. The more inventive the name, the more work you owe to make it understood.

## Capitalization

There is no iOS-sentence-case rule and no macOS-title-case rule. Apple's writing guidance is platform-unified. Casing is decided **per element type**, and several components have specific rules that you must follow:

| Element | Style |
|---|---|
| Button labels | Title-style, no ending punctuation |
| Menu items | Title-style |
| Alert title that is a complete sentence | Sentence-style, with ending punctuation |
| Alert title that is a sentence fragment | Title-style, no ending punctuation |
| Alert informative text | Complete sentences, sentence-style, normal punctuation |

For everything else, pick a style per element type and apply it consistently across the whole app.

Name onscreen elements exactly as they appear onscreen. If an element is all caps or all lowercase onscreen, use title-style when writing its name in documentation.

### Title-style algorithm

Capitalize:

- The first and last word, whatever part of speech
- Nouns, pronouns, verbs, adjectives, adverbs, however short: Is, Are, Be, It, This, You, Your, My
- Conjunctions other than coordinating ones, such as If
- Prepositions of five letters or more: About, Between, Through
- Prepositions of any length inside a phrasal verb (Turn On, Log In, Start Up) or serving as another part of speech
- The second word of a hyphenated compound, except Built-in and Plug-in

Do not capitalize:

- Articles a, an, the, unless first or following a colon
- Coordinating conjunctions: and, but, or, nor, for, yet, so
- The word "to" in an infinitive
- The word "as", always
- Names that always start lowercase: iPad, macOS, iPhone
- Prepositions of four letters or fewer: at, by, for, from, in, into, of, off, on, onto, out, over, to, up, with

Apple's examples: Skip This Backup · Apple News Is Offline · What to Do If Your iPhone Is Lost · Turn On Apple Watch · Log In to the Server · Export a Document as a PDF · Collaborate with Others · Restore iPhone from a Backup · High-Level Events · 64-Bit Addressing

## The ellipsis

Append an ellipsis when the action **requires more information before it can complete**. The trigger is needing input, not opening a window. A menu item that opens a view requiring no further input takes no ellipsis.

Use the real ellipsis character (…), not three periods.

In running prose, drop the ellipsis when naming the item: write "Choose File > New and click a template," never "Choose File > New… and click a template."

## Alerts

Alerts interrupt. Clear these gates before writing one:

- **Is it actionable?** If you only need to inform, find another way. An inline indicator beats a modal.
- **Is it uncommon and unrecoverable?** Do not alert for common destructive actions people can undo. Deleting one email needs no confirmation. Deleting an account does.
- **Is it at launch?** Never alert on app start. Show cached data with a quiet label instead.
- **Does it branch?** Alerts confirm or cancel. If you are offering choices about an intentional action, use an action sheet.

Copy rules:

- Be direct and neutral. Do not be oblique, do not be accusatory, and do not mask how bad the situation is.
- The title says what happened, in what context, and why. Never "Error." Never "Error 329347 occurred." Never more than two lines.
- Add informative text only if it adds value.
- Do not explain what the buttons do. If the title and the labels are clear, explaining them is noise.

Buttons:

- One or two words naming the **result**. Verbs tied to the alert text: View All, Reply, Ignore, Erase, Delete.
- **Never Yes or No.**
- **"OK" only in purely informational alerts.** Elsewhere it is ambiguous: does OK mean "yes, do it" or "I understand what would have happened"?
- The cancelling button is titled exactly **Cancel**.
- Read only the button labels. If the choice is still clear, they are good.

Structure:

- The trailing side of a row (top of a stack) is the default and the safe choice. Cancel usually sits leading.
- **A destructive button is never the default.** That is why a destructive verb takes the leading side and Cancel takes trailing.
- Every destructive action gets a Cancel button. If you want people to actually read the alert, give no button the default role.
- A single-button alert uses **Done**, not Cancel.
- Reserve destructive styling for destruction people did not deliberately choose. An "Empty Trash" button confirming the Empty Trash command does not need it.

**Never let a button verb collide with the dismissal verb.** Apple's worked failure: a dialog titled "Confirm Cancellation" with Cancel and Confirm buttons, where "cancel" means both "close this dialog" and "end my subscription." The fix names the object in the title and the verb in the buttons: "Cancel Platinum Subscription?" with **Cancel Subscription** and **Keep Subscription**.

## Component copy rules

**Buttons.** Start the label with a verb. On macOS, append a trailing ellipsis when the button opens another window, view, or app that needs more input. Keep prominent buttons to one or two per view. Never give the primary role to a destructive button, however likely it is, because prominence makes people press without reading. While an action runs, the label can change: Checkout becomes Checking out…

**Menu items.** Verb or verb phrase for actions. **Drop articles**: View Settings, not View the Settings. Articles lengthen labels and rarely add meaning. For a toggle, prefer one label that changes (Show Map becomes Hide Map) over two items. If a changing label is ambiguous between action and state, add a verb: "HDR On" could be either, "Turn HDR On" cannot. When one term repeats across three or more items in a group, use a submenu and keep the shared term in the parent label.

**Errors.** Put the message next to what broke. Avoid blame. Say what to do about it.

- "That password is too short" becomes "Choose a password with at least 8 characters."
- Instruct rather than scold: "Use only letters for your name" beats "Don't use numbers or symbols."
- "Invalid name" is the robotic anti-pattern. It tells people nothing.
- If language alone cannot fix an error that will hit many people, **the interaction is the problem**. Copy is not a patch for bad design.

**Empty states.** Name the absence, then explain how content arrives. Apple's model: "No Saved Episodes" with "Save episodes you want to listen to later, and they'll show up here." Give people an action they can take. Avoid whimsical idioms, which often do not translate and rarely help. Empty states are temporary, so never put important information only there.

**Settings.** Describe what the setting does when it is **on** and let people infer the off state. Do not describe where a setting lives. Link or navigate to it instead.

**Text fields.** Placeholder text should show a format ("name@example.com") or describe the content ("Your name"). Show errors next to the field.

**Multi-step flows.** Pick one vocabulary and hold it. "Get Started" opens, "Continue" or "Next" advances, "Done" closes. Mixing them mid-flow costs trust.

**Permission purpose strings.** The `Info.plist` usage description shown in a permission prompt. Say specifically what the app does with the resource, in one complete sentence: "Your location is used to show your position on the map, get directions, and estimate travel times." Not "This app needs your location." It must be a string and under 4,000 bytes. Add more only when it helps people decide whether to share personal data.

**Device verbs.** Match the input method. Never say "click" on a touch device where you mean "tap."

## Words Apple rules on

| Instead of | Use |
|---|---|
| we ("We're having trouble loading this content") | the passive or impersonal form ("Unable to load content"). Apple says avoid "we" altogether, since who "we" refers to is unclear |
| Your Favorites | Favorites. Use possessive pronouns sparingly, and never switch perspective mid-app |
| Please follow the steps below | Follow the steps below |
| click on, tap on | click, tap |
| click the mouse | press and release |
| select File > Open | **choose** File > Open. You *select* an object (a file, a message, some text), then *choose* a command |
| "click the checkbox" | Select or Deselect. You cannot know the checkbox's starting state |
| and/or | rewrite the sentence |
| abort | stop, quit, exit, interrupt |
| tooltip (in user-facing text) | help tag. "Tooltip" is for developer materials |
| Click here | a description of the destination: "Learn more about UX writing" |

**Contractions are recommended**, not merely tolerated. They are part of the informal voice. Keep localization in mind.

When Apple is silent, its own fallbacks are **The Chicago Manual of Style** for style and usage and **Merriam-Webster's Collegiate Dictionary** for spelling, in US English. Use those rather than another company's house style.

## Inclusive and accessible writing

This is a constraint on everything above, not an appendix.

- **Avoid violent, oppressive, and ableist technical metaphors**: kill, hang, master/slave, sanity check. In general, avoid describing software or hardware with human or biological attributes.
- **Avoid idioms and colloquialisms.** "Fall through the cracks," "on the same page," "backseat driver." They are harder to understand for people learning the language and harder to translate.
- **Do not use color to carry good or bad meaning.** No blacklist, whitelist, white hat, red team. Use color words for actual colors.
- **Singular they is correct.** "A subscriber can post their recipes." Apple marks "his or her" as incorrect. Never infer someone's pronouns from their name or appearance.
- **Disability language preferences vary.** Identity-first ("an autistic person") and person-first ("a person on the autism spectrum") are both used. Ask the individual or group; neither is a safe default. Never call nondisabled people normal, healthy, regular, or able-bodied. Do not describe people as brave or inspiring for having a disability.
- **Drop sense-dependent phrasing from instructions.** Not "you see a message" or "you hear an alert," but "A message appears" and "An alert sound plays."
- **Research a word you are unsure about**, both its origin and how people understand it now. If it is still questionable, pick another one.
- Use varied example names, and remember that not every culture uses one given name followed by one family name.

VoiceOver and image descriptions:

- An accessibility label **omits the control type**. The label for a Save button is "Save," not "Save button."
- Describe images with both the physical detail and the intention. Apple's own: "Person tilting head to the side with hand beside mouth as if sharing a secret."
- Use "person," not a gendered noun, unless gender is genuinely part of the content.

## Keep a word list

One term per concept, chosen once and used everywhere. A table works: the word you use, the words you do not, and a one-line definition.

| Use | Not | Meaning |
|---|---|---|
| alias | handle, user name, title | The player's in-game name, shown to other players. Not used to sign in. |
| health | lives, hearts, energy, stamina | Measure of player longevity. |

Include button labels. The same action gets the same word every time it appears. Build the list one word at a time as you go rather than trying to write it all at once.

## Before you call it done

- [ ] **Read it out loud.** This is Apple's most-repeated advice, appearing in three of four WWDC writing sessions and in the HIG. It catches filler, repetition, grammar, typos, and anything that does not sound like a person.
- [ ] Every filler adverb, adjective, interjection, and pleasantry is gone or justified.
- [ ] Headline and body do not say the same thing twice.
- [ ] The benefit is at the front of the sentence, not the end.
- [ ] Button labels are verbs naming the result, in title-style, with no ending punctuation.
- [ ] Reading only the button labels, the choice is still clear.
- [ ] No Yes/No. No bare "OK" outside a purely informational alert.
- [ ] No button verb collides with "Cancel."
- [ ] Ellipses appear only where more input is required.
- [ ] Alert titles follow the sentence-vs-fragment casing rule.
- [ ] No "we." Possessive pronouns are sparse and consistent.
- [ ] Device verbs match the device.
- [ ] Every label bound to data was checked at its worst-case value.
- [ ] Terms match the word list.
- [ ] No idioms, no color-coded meaning, no sense-dependent instructions.

## Sources

- [HIG: Writing](https://developer.apple.com/design/human-interface-guidelines/writing) and the component pages for [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts), [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons), and [Menus](https://developer.apple.com/design/human-interface-guidelines/menus)
- [Apple Style Guide](https://support.apple.com/guide/applestyleguide/welcome/web), free and public, including its Writing Inclusively chapter. The HIG's "Writing inclusively" link points here, not to a HIG page.
- WWDC sessions, one framework each: [Writing for interfaces](https://developer.apple.com/videos/play/wwdc2022/10037/) (PACE), [Add personality to your app through UX writing](https://developer.apple.com/videos/play/wwdc2024/10140/) (voice and tone), [Make a big impact with small writing changes](https://developer.apple.com/videos/play/wwdc2025/404/) (the four edits), [Craft clear names for features and labels in your app](https://developer.apple.com/videos/play/wwdc2026/290/) (naming)

For general UX writing principles outside Apple platforms, see the `better-writing` skill.
