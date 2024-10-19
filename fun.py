import streamlit as st

# All 20 topics from the Cosmic Chronicles book
topics = {
    "The Big Bang – The Birth of the Universe": "The Big Bang marks the beginning of the universe, about 13.8 billion years ago. It was an explosion of energy that gave birth to everything we see today.",
    "Black Holes – The Cosmic Vacuum Cleaners": "Black holes are regions in space with such strong gravity that nothing, not even light, can escape. They form when massive stars collapse under their own gravity.",
    "Dark Matter – The Invisible Force": "Dark matter is an invisible form of matter that does not emit or interact with electromagnetic radiation, making it undetectable by conventional means.",
    "The Theory of Relativity – Time and Space Intertwined": "Einstein's theory of relativity shows how time and space are interconnected and how gravity affects the passage of time.",
    "Quantum Mechanics – The World of the Very Small": "Quantum mechanics governs the behavior of particles on an atomic and subatomic level, where the traditional laws of physics no longer apply.",
    "Time Travel – Possibilities and Paradoxes": "Time travel is theoretically possible through mechanisms like wormholes, but it introduces paradoxes such as the grandfather paradox.",
    "The Expanding Universe – A Cosmic Mystery": "The universe has been expanding since the Big Bang, with galaxies moving farther apart. This expansion is speeding up due to dark energy.",
    "The Multiverse – Are We Alone?": "The multiverse theory suggests that our universe may be one of many, each with different physical laws and conditions.",
    "The Lifecycle of Stars – From Birth to Supernova": "Stars go through a life cycle, from birth in stellar nurseries to eventual collapse or explosion in supernovae.",
    "The Fate of the Universe – Scenarios for the End": "The fate of the universe could involve a Big Freeze, Big Crunch, or Big Rip, depending on the forces at play, particularly dark energy.",
    "The Electromagnetic Spectrum – Light Beyond What We See": "The electromagnetic spectrum covers all types of light waves, from radio waves to gamma rays, including the visible light we can see.",
    "Gravitational Waves – Ripples in Space-Time": "Gravitational waves are ripples in the fabric of space-time caused by cataclysmic events such as colliding black holes.",
    "Supernovae – The Explosive Death of Stars": "Supernovae are massive explosions marking the death of stars, releasing enormous amounts of energy and producing heavy elements.",
    "Neutron Stars – Cosmic Giants in Tiny Packages": "Neutron stars are incredibly dense objects formed from the remnants of supernovae, with a mass greater than the Sun packed into a small radius.",
    "Exoplanets – Worlds Beyond Our Solar System": "Exoplanets are planets that orbit stars outside our solar system, with some potentially located in habitable zones where life could exist.",
    "The Drake Equation – The Search for Extraterrestrial Life": "The Drake Equation estimates the number of civilizations in our galaxy that could communicate with us, considering factors like the number of habitable planets.",
    "Cosmic Inflation – The Universe’s Growth Spurt": "Cosmic inflation refers to the rapid expansion of the universe in its earliest moments, explaining why the universe is so large and uniform.",
    "Antimatter – The Mirror of Matter": "Antimatter consists of particles that are the opposite of normal matter. When matter and antimatter meet, they annihilate each other, producing energy.",
    "Dark Energy – The Force Behind the Expanding Universe": "Dark energy is a mysterious force causing the accelerated expansion of the universe, making up roughly 70% of its total energy.",
    "The Higgs Boson – The Particle That Gives Mass": "The Higgs boson is the particle that gives mass to other particles, confirmed by experiments at the Large Hadron Collider in 2012."
}

# Questions and Answers for each topic
qa_data = {
    "The Big Bang – The Birth of the Universe": [
        ("What is the Big Bang?", "The Big Bang is the theory that the universe began as a single point and has been expanding ever since."),
        ("How old is the universe?", "The universe is approximately 13.8 billion years old."),
        ("Who discovered the expanding universe?", "Edwin Hubble discovered that the universe is expanding in the 1920s."),
        ("What is cosmic microwave background radiation?", "Cosmic microwave background (CMB) is the leftover radiation from the Big Bang, providing a snapshot of the early universe."),
        ("What does Hubble's Law state?", "Hubble's Law states that the farther away a galaxy is, the faster it moves away from us.")
    ],
    "Black Holes – The Cosmic Vacuum Cleaners": [
        ("What is a black hole?", "A black hole is a region in space where gravity is so strong that nothing, not even light, can escape."),
        ("How are black holes formed?", "Black holes are formed when massive stars collapse under their own gravity."),
        ("What is the event horizon?", "The event horizon is the boundary around a black hole beyond which nothing can escape."),
        ("Can black holes shrink?", "Yes, black holes can lose energy and shrink through a process called Hawking radiation."),
        ("Who predicted the existence of black holes?", "Black holes were predicted by Einstein's theory of General Relativity.")
    ],
    # Similar Q&A data for other topics...
    "Dark Matter – The Invisible Force": [
        ("What is dark matter?", "Dark matter is an invisible form of matter that exerts gravitational effects on galaxies but does not emit light."),
        ("How do we detect dark matter?", "We detect dark matter through its gravitational effects on visible matter, like stars and galaxies."),
        ("How much of the universe is dark matter?", "Dark matter makes up about 27% of the universe."),
        ("Why is dark matter important?", "Dark matter is important because it holds galaxies together; without it, they would fly apart."),
        ("Can dark matter be seen?", "No, dark matter cannot be seen directly as it does not interact with light.")
    ],
     "The Theory of Relativity – Time and Space Intertwined": [
        ("What is the theory of relativity?", "The theory of relativity, proposed by Einstein, explains how time and space are linked and how gravity can affect time."),
        ("What is time dilation?", "Time dilation is a phenomenon where time moves slower in stronger gravitational fields or for objects moving close to the speed of light."),
        ("What are the two parts of relativity?", "The two parts are special relativity, which deals with high speeds, and general relativity, which deals with gravity and curved space-time."),
        ("What does E=mc² mean?", "E=mc² is Einstein's famous equation that shows the relationship between energy (E), mass (m), and the speed of light (c)."),
        ("How does gravity affect time?", "Gravity causes time to slow down; this is known as gravitational time dilation.")
    ],
    "Quantum Mechanics – The World of the Very Small": [
        ("What is quantum mechanics?", "Quantum mechanics is the branch of physics that studies the behavior of particles at the atomic and subatomic levels."),
        ("What is the uncertainty principle?", "The uncertainty principle states that you cannot know both the position and velocity of a particle with absolute precision."),
        ("What is quantum entanglement?", "Quantum entanglement is a phenomenon where two particles become connected, and changes in one affect the other, even over large distances."),
        ("What is a quantum leap?", "A quantum leap refers to the sudden change in an electron's energy level within an atom."),
        ("Who are some key figures in quantum mechanics?", "Some key figures include Max Planck, Niels Bohr, and Albert Einstein.")
    ],
    "Time Travel – Possibilities and Paradoxes": [
        ("What is time travel?", "Time travel refers to the concept of moving through time, either to the past or future, by manipulating space-time."),
        ("What is the grandfather paradox?", "The grandfather paradox is a hypothetical situation where a time traveler prevents their own existence by altering past events."),
        ("What is a wormhole?", "A wormhole is a theoretical tunnel in space-time that could connect two distant points, potentially allowing time travel."),
        ("Is time travel possible?", "While time travel is a popular concept in science fiction, it remains purely theoretical with no experimental evidence."),
        ("Can black holes enable time travel?", "Some theories suggest that rotating black holes could theoretically allow time travel, but it is highly speculative.")
    ],
    "The Expanding Universe – A Cosmic Mystery": [
        ("Is the universe expanding?", "Yes, the universe has been expanding ever since the Big Bang."),
        ("What is dark energy?", "Dark energy is a mysterious force causing the universe's expansion to accelerate."),
        ("What is the rate of expansion?", "The rate of expansion is described by Hubble's constant."),
        ("What evidence do we have for the expanding universe?", "The redshift of light from distant galaxies shows they are moving away, providing evidence for the expansion."),
        ("Will the universe continue to expand?", "Current evidence suggests the universe will continue to expand indefinitely, possibly ending in a 'Big Freeze.'")
    ],
    "The Multiverse – Are We Alone?": [
        ("What is the multiverse?", "The multiverse theory suggests that our universe is one of many, each with different physical laws."),
        ("What evidence supports the multiverse?", "There is no direct evidence for the multiverse, but it is a prediction of certain cosmological models like cosmic inflation."),
        ("What is cosmic inflation?", "Cosmic inflation is the rapid expansion of the universe immediately after the Big Bang, which could create multiple universes."),
        ("Are the laws of physics the same in all universes?", "According to the multiverse theory, different universes could have entirely different physical laws."),
        ("Who proposed the multiverse theory?", "The idea of a multiverse has been explored by various scientists, including Hugh Everett and Alan Guth.")
    ],
    "The Lifecycle of Stars – From Birth to Supernova": [
        ("How do stars form?", "Stars form from clouds of gas and dust in space called nebulae."),
        ("What is a main-sequence star?", "A main-sequence star is a stable star that fuses hydrogen into helium in its core."),
        ("What happens when a star dies?", "When a star exhausts its nuclear fuel, it can collapse into a white dwarf, neutron star, or black hole, depending on its mass."),
        ("What is a supernova?", "A supernova is a massive explosion that marks the death of a star."),
        ("What elements are created in supernovae?", "Supernovae produce heavy elements like iron, gold, and uranium.")
    ],
    "The Fate of the Universe – Scenarios for the End": [
        ("What are possible fates of the universe?", "Possible fates include the Big Freeze, Big Crunch, and Big Rip."),
        ("What is the Big Freeze?", "The Big Freeze is a scenario where the universe continues expanding until stars burn out and the universe becomes cold and dark."),
        ("What is the Big Crunch?", "The Big Crunch is the idea that the universe could stop expanding and collapse in on itself."),
        ("What is the Big Rip?", "The Big Rip is a hypothesis where dark energy causes the universe to expand so quickly that everything, even atoms, is torn apart."),
        ("How does dark energy affect the fate of the universe?", "Dark energy is accelerating the expansion of the universe, making a Big Freeze or Big Rip more likely.")
    ],
    "The Electromagnetic Spectrum – Light Beyond What We See": [
        ("What is the electromagnetic spectrum?", "The electromagnetic spectrum is the range of all types of electromagnetic radiation, from radio waves to gamma rays."),
        ("What is visible light?", "Visible light is the portion of the electromagnetic spectrum that humans can see."),
        ("What are radio waves?", "Radio waves are a type of electromagnetic radiation with long wavelengths used for communication."),
        ("What are gamma rays?", "Gamma rays are the highest-energy form of electromagnetic radiation, often produced by supernovae or black holes."),
        ("How do X-rays work?", "X-rays are a form of high-energy radiation used in medical imaging to see inside the body.")
    ],
    "Gravitational Waves – Ripples in Space-Time": [
        ("What are gravitational waves?", "Gravitational waves are ripples in space-time caused by the acceleration of massive objects."),
        ("Who predicted gravitational waves?", "Gravitational waves were predicted by Albert Einstein in his theory of general relativity."),
        ("How are gravitational waves detected?", "Gravitational waves are detected by instruments like LIGO, which measure tiny distortions in space-time."),
        ("What causes gravitational waves?", "Gravitational waves are caused by events such as colliding black holes or neutron stars."),
        ("When were gravitational waves first detected?", "Gravitational waves were first detected in 2015 by LIGO.")
    ],
    "Supernovae – The Explosive Death of Stars": [
        ("What is a supernova?", "A supernova is the explosive death of a star, releasing massive amounts of energy."),
        ("What types of supernovae are there?", "There are two main types: Type I, which occurs in binary star systems, and Type II, which occurs in massive stars."),
        ("What elements are produced in a supernova?", "Supernovae produce heavy elements like iron, gold, and uranium."),
        ("Can we see supernovae from Earth?", "Yes, supernovae can sometimes be seen from Earth as extremely bright points in the sky."),
        ("What is a supernova remnant?", "A supernova remnant is the expanding shell of gas and dust left behind after a supernova explosion.")
    ],
    "Neutron Stars – Cosmic Giants in Tiny Packages": [
        ("What is a neutron star?", "A neutron star is a dense remnant of a supernova, composed mostly of neutrons."),
        ("How dense are neutron stars?", "Neutron stars are incredibly dense; a teaspoon of neutron star material would weigh billions of tons."),
        ("What is a pulsar?", "A pulsar is a rapidly rotating neutron star that emits beams of radiation."),
        ("How large are neutron stars?", "Neutron stars are typically about 20 kilometers in diameter but have more mass than the Sun."),
        ("What causes a neutron star?", "A neutron star forms when the core of a massive star collapses after a supernova.")
    ],
    "Exoplanets – Worlds Beyond Our Solar System": [
        ("What is an exoplanet?", "An exoplanet is a planet that orbits a star outside our solar system."),
        ("How are exoplanets detected?", "Exoplanets are detected using methods like the transit method and radial velocity method."),
        ("What is the habitable zone?", "The habitable zone is the region around a star where conditions might be right for liquid water to exist."),
        ("Can exoplanets support life?", "Some exoplanets in the habitable zone could potentially support life, but no definitive evidence has been found."),
        ("What is the most famous exoplanet?", "One of the most famous exoplanets is Kepler-186f, which is located in the habitable zone of its star.")
    ],
    "The Drake Equation – The Search for Extraterrestrial Life": [
        ("What is the Drake Equation?", "The Drake Equation estimates the number of civilizations in our galaxy that could communicate with us."),
        ("What factors are considered in the Drake Equation?", "The equation considers factors like the number of habitable planets and the likelihood of intelligent life."),
        ("Who proposed the Drake Equation?", "The Drake Equation was proposed by astronomer Frank Drake in 1961."),
        ("What is the significance of the Drake Equation?", "The Drake Equation helps scientists estimate the chances of finding intelligent extraterrestrial life."),
        ("Has the Drake Equation been solved?", "No, the Drake Equation has many unknown variables, so it remains a tool for estimation rather than a definitive answer.")
    ],
    "Cosmic Inflation – The Universe’s Growth Spurt": [
        ("What is cosmic inflation?", "Cosmic inflation is the rapid expansion of the universe in the first fractions of a second after the Big Bang."),
        ("Who proposed cosmic inflation?", "The theory of cosmic inflation was proposed by physicist Alan Guth in 1980."),
        ("Why is cosmic inflation important?", "Cosmic inflation helps explain the large-scale structure and uniformity of the universe."),
        ("What evidence supports cosmic inflation?", "The uniformity of the cosmic microwave background radiation supports the theory of cosmic inflation."),
        ("What happened after inflation?", "After inflation, the universe continued to expand at a slower rate and began cooling, leading to the formation of matter.")
    ],
    "Antimatter – The Mirror of Matter": [
        ("What is antimatter?", "Antimatter consists of particles that are the opposite of normal matter, with opposite charges."),
        ("What happens when matter and antimatter meet?", "When matter and antimatter meet, they annihilate each other, producing energy."),
        ("Why is there more matter than antimatter?", "The imbalance between matter and antimatter is one of the great mysteries of the universe."),
        ("Can we create antimatter?", "Yes, antimatter can be created in particle accelerators, but it is difficult and expensive to produce."),
        ("Where is antimatter found?", "Antimatter is rare in the universe and is mostly found in high-energy environments like around black holes or in cosmic rays.")
    ],
    "Dark Energy – The Force Behind the Expanding Universe": [
        ("What is dark energy?", "Dark energy is a mysterious force causing the accelerated expansion of the universe."),
        ("How much of the universe is dark energy?", "Dark energy makes up about 70% of the universe."),
        ("What evidence is there for dark energy?", "The accelerating expansion of the universe, as observed through distant supernovae, provides evidence for dark energy."),
        ("What is the cosmological constant?", "The cosmological constant is a term in Einstein's equations that could explain dark energy as a property of space itself."),
        ("How does dark energy affect the universe?", "Dark energy is driving the universe's expansion at an increasing rate, potentially leading to a Big Rip scenario.")
    ],
    "The Higgs Boson – The Particle That Gives Mass": [
        ("What is the Higgs boson?", "The Higgs boson is a particle that gives mass to other particles through the Higgs field."),
        ("When was the Higgs boson discovered?", "The Higgs boson was discovered in 2012 at the Large Hadron Collider."),
        ("What is the Higgs field?", "The Higgs field is a field that exists throughout the universe, and particles gain mass by interacting with it."),
        ("Why is the Higgs boson important?", "The discovery of the Higgs boson confirmed the Standard Model of particle physics."),
        ("Who predicted the existence of the Higgs boson?", "The Higgs boson was predicted by physicist Peter Higgs and others in the 1960s.")
    ]
}

# Home Page Title & Introduction
st.title("Cosmic Chronicles: Unraveling the Mysteries of the Universe")
st.write("Welcome to the Cosmic Chronicles companion website. Explore various cosmic phenomena and get answers to your questions about the universe.")

# Dropdown to explore topics
st.subheader("Explore Topics")
selected_topic = st.selectbox("Choose a chapter to explore", list(topics.keys()))

# Display the content of the selected topic
if selected_topic:
    st.write(f"### {selected_topic}")
    st.write(topics[selected_topic])

# Dropdown for Questions
if selected_topic:
    st.subheader(f"Choose a question about {selected_topic}")
    selected_question = st.selectbox("Select a question", [q for q, a in qa_data[selected_topic]])

    # Display the answer for the selected question
    if selected_question:
        for q, a in qa_data[selected_topic]:
            if selected_question == q:
                st.write(f"**Q:** {q}")
                st.write(f"**A:** {a}")
                break

# Footer
st.write("### Thank you for exploring the universe with Cosmic Chronicles!")

# To run this app:
# 1. Save this script as `app.py`.
# 2. In the terminal, run: streamlit run app.py
